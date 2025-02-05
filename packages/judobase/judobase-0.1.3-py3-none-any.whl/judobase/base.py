from aiohttp import ClientSession
from judobase.schemas import Competition, Contest, Judoka, Country

BASE_URL = "https://data.ijf.org/api/"
HTTP_STATUS_OK = 200

class _Base:
    """Base class for API interaction with session management."""

    def __init__(self):
        self._session = ClientSession()

    async def __aenter__(self):
        """Enter async context and create session if needed."""
        if self._session.closed:
            self._session = ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Exit async context and close session."""
        await self.close_session()

    async def close_session(self):
        """Close session if open."""
        if not self._session.closed:
            await self._session.close()

    async def _get_json(self, request_params) -> dict:
        """Helper method to send a GET request and return JSON."""
        response = await self._session.get(
            f"{BASE_URL}get_json",
            timeout=10,
            params=request_params,
        )
        if response.status != HTTP_STATUS_OK:
            raise ConnectionError(f"{response.status}")
        return await response.json()


class CompetitionAPI(_Base):
    """Handles competition-related API requests."""

    async def get_competition_list(self, years: str = "", months: str = "") -> list[Competition]:
        """Fetches list of competitions."""
        return [
            Competition(**comp)
            for comp in await self._get_json(
                request_params={
                    "params[action]": "competition.get_list",
                    "params[year]": years,
                    "params[month]": months,
                    "params[sort]": -1,
                    "params[limit]": 5000,
                }
            )
        ]

    async def get_competition_info(self, id_competition: str) -> Competition:
        """Fetches details of a specific competition."""
        return Competition(
            **await self._get_json(
                request_params={
                    "params[action]": "competition.info",
                    "params[id_competition]": id_competition,
                }
            )
        )


class ContestAPI(_Base):
    """Handles contest-related API requests."""

    async def find_contests(self, id_competition: str = "", id_weight: str = "", id_person: str = "") -> list[Contest]:
        """Fetches list of contests."""
        request_result = await self._get_json(
            request_params={
                "params[action]": "contest.find",
                "params[id_competition]": id_competition,
                "params[id_weight]": id_weight,
                "params[id_person]": id_person,
                "params[order_by]": "cnum",
                "params[limit]": 5000,
            }
        )
        return [Contest(**contest) for contest in request_result["contests"]]


class JudokaAPI(_Base):
    """Handles judoka-related API requests."""

    async def get_judoka_info(self, id_competitor: str) -> Judoka:
        """Fetches judoka information."""
        return Judoka(
            **await self._get_json(
                request_params={
                    "params[action]": "competitor.info",
                    "params[id_person]": id_competitor,
                }
            )
        )


class CountryAPI(_Base):
    """Handles country-related API requests."""

    async def get_country_info(self, id_country: str) -> Country:
        """Fetches country information."""
        return Country(
            **await self._get_json(
                request_params={
                    "params[action]": "country.info",
                    "params[id_country]": id_country,
                }
            )
        )
