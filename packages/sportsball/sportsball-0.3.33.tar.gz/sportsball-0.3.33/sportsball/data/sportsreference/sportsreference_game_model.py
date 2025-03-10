"""Sports Reference game model."""

# pylint: disable=too-many-locals,too-many-statements,unused-argument,protected-access,too-many-arguments
import datetime
import io
import logging
import urllib.parse

import dateutil
import pandas as pd
import pytest_is_running
import requests_cache
from bs4 import BeautifulSoup, Tag
from dateutil.parser import parse

from ...cache import MEMORY
from ..game_model import GameModel
from ..league import League
from ..season_type import SeasonType
from ..team_model import TeamModel
from .sportsreference_team_model import create_sportsreference_team_model
from .sportsreference_venue_model import create_sportsreference_venue_model


def _find_old_dt(
    dfs: list[pd.DataFrame],
    session: requests_cache.CachedSession,
    soup: BeautifulSoup,
    url: str,
    league: League,
    player_urls: set[str],
    fg: dict[str, int],
    fga: dict[str, int],
    offensive_rebounds: dict[str, int],
    assists: dict[str, int],
    turnovers: dict[str, int],
) -> tuple[datetime.datetime, list[TeamModel], str]:
    teams: list[TeamModel] = []
    dt = None
    venue_name = None
    for df in dfs:
        test_row = df.iat[0, 0]
        if "Prev Game" in test_row and len(df) == 2:
            date_venue_split = df.iat[1, 0].split()
            dt = parse(" ".join(date_venue_split[:5]))
            venue_name = " ".join(date_venue_split[5:])
            for col_idx in range(len(df.columns.values)):
                team_row = df.iat[0, col_idx]
                team_name_points = team_row.split("⇐")[0].strip()
                points = int(team_name_points.split()[-1].strip())
                team_name = " ".join(team_name_points.split()[:-1]).strip()
                team_a = soup.find("a", text=team_name, href=True)
                if not isinstance(team_a, Tag):
                    raise ValueError("team_a is not a tag.")
                team_url = urllib.parse.urljoin(url, str(team_a.get("href")))
                teams.append(
                    create_sportsreference_team_model(
                        session,
                        team_url,
                        dt,
                        league,
                        player_urls,
                        points,
                        fg,
                        fga,
                        offensive_rebounds,
                        assists,
                        turnovers,
                    )
                )
            break

    if dt is None:
        raise ValueError("dt is null.")
    if venue_name is None:
        raise ValueError("venue_name is null.")

    return (dt, teams, venue_name)


def _find_new_dt(
    soup: BeautifulSoup,
    scorebox_meta_div: Tag,
    url: str,
    session: requests_cache.CachedSession,
    league: League,
    player_urls: set[str],
    scores: list[float],
    fg: dict[str, int],
    fga: dict[str, int],
    offensive_rebounds: dict[str, int],
    assists: dict[str, int],
    turnovers: dict[str, int],
) -> tuple[datetime.datetime, list[TeamModel], str]:
    in_divs = scorebox_meta_div.find_all("div")
    current_in_div_idx = 0
    in_div = in_divs[current_in_div_idx]
    in_div_text = in_div.get_text().strip()
    current_in_div_idx += 1
    if "Tournament" in in_div_text:
        in_div_text = in_divs[1].get_text().strip()
        current_in_div_idx += 1
    try:
        dt = parse(in_div_text)
    except dateutil.parser._parser.ParserError as exc:  # type: ignore
        logging.error("Failed to parse date for URL: %s", url)
        raise exc
    venue_div = in_divs[current_in_div_idx]
    venue_name = venue_div.get_text().strip()
    scorebox_div = soup.find("div", class_="scorebox")
    if not isinstance(scorebox_div, Tag):
        raise ValueError("scorebox_div is not a Tag.")

    teams: list[TeamModel] = []
    for a in scorebox_div.find_all("a"):
        team_url = urllib.parse.urljoin(url, a.get("href"))
        if "/schools/" in team_url:
            teams.append(
                create_sportsreference_team_model(
                    session,
                    team_url,
                    dt,
                    league,
                    player_urls,
                    scores[len(teams)],
                    fg,
                    fga,
                    offensive_rebounds,
                    assists,
                    turnovers,
                )
            )

    return (dt, teams, venue_name)


def _create_sportsreference_game_model(
    session: requests_cache.CachedSession,
    url: str,
    league: League,
) -> GameModel:
    # pylint: disable=too-many-branches
    response = session.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    player_urls = set()
    for a in soup.find_all("a"):
        player_url = urllib.parse.urljoin(url, a.get("href"))
        if "/players/" in player_url and not player_url.endswith("/players/"):
            player_urls.add(player_url)

    scores = []
    for score_div in soup.find_all("div", class_="score"):
        scores.append(float(score_div.get_text().strip()))

    handle = io.StringIO()
    handle.write(response.text)
    handle.seek(0)
    dfs = pd.read_html(handle)
    fg = {}
    fga = {}
    offensive_rebounds = {}
    assists = {}
    turnovers = {}
    for df in dfs:
        if df.index.nlevels > 1:
            df.columns = df.columns.get_level_values(1)
        if "Starters" in df.columns.values:
            players = df["Starters"].tolist()
            if "FG" in df.columns.values:
                fgs = df["FG"].tolist()
                for idx, player in enumerate(players):
                    fg[player] = fgs[idx]
            if "FGA" in df.columns.values:
                fgas = df["FGA"].tolist()
                for idx, player in enumerate(players):
                    fga[player] = fgas[idx]
            if "OREB" in df.columns.values:
                orebs = df["OREB"].tolist()
                for idx, player in enumerate(players):
                    offensive_rebounds[player] = orebs[idx]
            if "AST" in df.columns.values:
                asts = df["AST"].tolist()
                for idx, player in enumerate(players):
                    assists[player] = asts[idx]
            if "TOV" in df.columns.values:
                tovs = df["TOV"].tolist()
                for idx, player in enumerate(players):
                    turnovers[player] = tovs[idx]

    scorebox_meta_div = soup.find("div", class_="scorebox_meta")
    if not isinstance(scorebox_meta_div, Tag):
        dt, teams, venue_name = _find_old_dt(
            dfs,
            session,
            soup,
            url,
            league,
            player_urls,
            fg,
            fga,
            offensive_rebounds,
            assists,
            turnovers,
        )
    else:
        dt, teams, venue_name = _find_new_dt(
            soup,
            scorebox_meta_div,
            url,
            session,
            league,
            player_urls,
            scores,
            fg,
            fga,
            offensive_rebounds,
            assists,
            turnovers,
        )

    season_type = SeasonType.REGULAR
    for h2 in soup.find_all("h2"):
        a = h2.find("a")
        if a is None:
            continue
        season_text = a.get_text().strip()
        match season_text:
            case "Big Sky Conference":
                season_type = SeasonType.REGULAR
            case "Big East Conference":
                season_type = SeasonType.REGULAR
            case "Big West Conference":
                season_type = SeasonType.REGULAR
            case "Big Ten Conference":
                season_type = SeasonType.REGULAR
            case "Mid-American Conference":
                season_type = SeasonType.REGULAR
            case "Horizon League":
                season_type = SeasonType.REGULAR
            case "Atlantic 10 Conference":
                season_type = SeasonType.REGULAR
            case "Mountain West Conference":
                season_type = SeasonType.REGULAR
            case "West Coast Conference":
                season_type = SeasonType.REGULAR
            case "American Athletic Conference":
                season_type = SeasonType.REGULAR
            case "Coastal Athletic Association":
                season_type = SeasonType.REGULAR
            case "Conference USA":
                season_type = SeasonType.REGULAR
            case "America East Conference":
                season_type = SeasonType.REGULAR
            case "Sun Belt Conference":
                season_type = SeasonType.REGULAR
            case "Metro Atlantic Athletic Conference":
                season_type = SeasonType.REGULAR
            case "Atlantic Sun Conference":
                season_type = SeasonType.REGULAR
            case "Ohio Valley Conference":
                season_type = SeasonType.REGULAR
            case "Mid-Eastern Athletic Conference":
                season_type = SeasonType.REGULAR
            case "Big South Conference":
                season_type = SeasonType.REGULAR
            case "Summit League":
                season_type = SeasonType.REGULAR
            case "Western Athletic Conference":
                season_type = SeasonType.REGULAR
            case "Big 12 Conference":
                season_type = SeasonType.REGULAR
            case "Southeastern Conference":
                season_type = SeasonType.REGULAR
            case "Patriot League":
                season_type = SeasonType.REGULAR
            case "Southern Conference":
                season_type = SeasonType.REGULAR
            case "Missouri Valley Conference":
                season_type = SeasonType.REGULAR
            case "Atlantic Coast Conference":
                season_type = SeasonType.REGULAR
            case "Southwest Athletic Conference":
                season_type = SeasonType.REGULAR
            case "Southland Conference":
                season_type = SeasonType.REGULAR
            case "Northeast Conference":
                season_type = SeasonType.REGULAR
            case "Ivy League":
                season_type = SeasonType.REGULAR
            case "NCAA Men's Tournament":
                season_type = SeasonType.REGULAR
            case "Pac-12 Conference":
                season_type = SeasonType.REGULAR
            case _:
                logging.warning("Unrecognised Season Text: %s", season_text)
        break

    return GameModel(
        dt=dt,
        week=None,
        game_number=None,
        venue=create_sportsreference_venue_model(venue_name, session, dt),  # pyright: ignore
        teams=teams,
        league=league,
        year=dt.year,
        season_type=season_type,
        end_dt=None,
        attendance=None,
        postponed=None,
        play_off=None,
    )


@MEMORY.cache(ignore=["session"])
def _cached_create_sportsreference_game_model(
    session: requests_cache.CachedSession,
    url: str,
    league: League,
) -> GameModel:
    return _create_sportsreference_game_model(session, url, league)


def create_sportsreference_game_model(
    session: requests_cache.CachedSession,
    url: str,
    league: League,
    dt: datetime.datetime,
) -> GameModel:
    """Create a sports reference game model."""
    if not pytest_is_running.is_running():
        return _cached_create_sportsreference_game_model(session, url, league)
    with session.cache_disabled():
        return _create_sportsreference_game_model(session, url, league)
