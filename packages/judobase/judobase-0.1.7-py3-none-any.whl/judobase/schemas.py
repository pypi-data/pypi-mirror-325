"""Defines Pydantic models for the data provided by the Judobase API.

classes:
- Judoka: Represents the data about a judoka.
- Competition: Represents the data about a competition.
- Contest: Represents the data about a contest.
- Country: Represents the data about a country.
"""

# flake8: noqa: WPS110, WPS114

from datetime import datetime, timezone
from typing import Any

from pydantic import BaseModel, Field, field_validator


class Competition(BaseModel):
    """Represents the data about competition which provide the judobase api."""

    id_competition: str = Field(
        ..., title="Competition ID", description="The unique identifier for the competition."
    )
    date_from: str = Field(
        ...,
        title="Start Date",
        description="The start date of the competition in YYYY/MM/DD format.",
    )
    date_to: str = Field(
        ..., title="End Date", description="The end date of the competition in YYYY/MM/DD format."
    )
    name: str = Field(..., title="Competition Name", description="The name of the competition.")
    has_results: int = Field(
        None, title="Results Available", description="Indicates if results are available."
    )
    city: str = Field(..., title="City", description="The city where the competition is held.")
    street: str = Field(
        None, title="Street", description="The street where the competition venue is located."
    )
    street_no: str = Field(
        None, title="Street Number", description="The street number of the competition venue."
    )
    comp_year: int = Field(
        None, title="Competition Year", description="The year in which the competition takes place."
    )
    prime_event: bool = Field(
        None, title="Prime Event", description="Indicates if this is a prime event."
    )
    continent_short: str = Field(
        None, title="Continent Code", description="The short code for the continent."
    )
    has_logo: bool = Field(
        False, title="Has Logo", description="Indicates if the competition has a logo."
    )
    competition_code: str | None = Field(
        None, title="Competition Code", description="The unique code for the competition."
    )
    updated_at_ts: datetime = Field(
        ..., title="Last Updated Timestamp", description="The timestamp of the last update."
    )
    updated_at: datetime = Field(
        None, title="Last Updated", description="The last update date and time."
    )
    timezone: str | None = Field(
        None, title="Timezone", description="The timezone of the competition."
    )
    id_live_theme: int = Field(
        ..., title="Live Theme ID", description="The ID of the live theme used for the competition."
    )
    code_live_theme: str = Field(
        ..., title="Live Theme Code", description="The code of the live theme used."
    )
    country_short: str = Field(
        ..., title="Country Short Code", description="The short code for the country."
    )
    country: str = Field(
        ..., title="Country", description="The country where the competition is held."
    )
    id_country: int = Field(
        ..., title="Country ID", description="The unique identifier for the country."
    )
    is_teams: int = Field(
        ..., title="Team Competition", description="Indicates if the competition is a team event."
    )
    status: str | None = Field(None, title="Status", description="The status of the competition.")
    external_id: str | None = Field(
        None, title="External ID", description="The external identifier for the competition."
    )
    id_draw_type: int = Field(None, title="Draw Type ID", description="The ID of the draw type.")
    ages: list[str] = Field(
        None, title="Age Categories", description="List of age categories for the competition."
    )
    rank_name: str | None = Field(
        None, title="Ranking Name", description="The ranking name associated with the competition."
    )

    @field_validator("updated_at", mode="after")
    @classmethod
    def parse_updated_at(cls, value):
        """Converts the `updated_at` field to a datetime object with UTC timezone."""
        return value.replace(tzinfo=timezone.utc)

    @field_validator("date_from", mode="after")
    @classmethod
    def parse_date_from(cls, value):
        """Converts the `date_from` field to a datetime object with UTC timezone."""
        try:
            return datetime.strptime(value, "%Y/%m/%d").replace(tzinfo=timezone.utc)
        except ValueError:
            return datetime.strptime(value, "%Y-%m-%d").replace(tzinfo=timezone.utc)

    @field_validator("date_to", mode="after")
    @classmethod
    def parse_date_to(cls, value):
        """Converts the `date_to` field to a datetime object with UTC timezone."""
        if isinstance(value, str):
            try:
                return datetime.strptime(value, "%Y/%m/%d").replace(tzinfo=timezone.utc)
            except ValueError:
                return datetime.strptime(value, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        return None


class Contest(BaseModel):
    """Represents the data about contest which provide the judobase api."""

    # General contest data
    id_competition: str = Field(
        ..., title="Competition ID", description="The unique identifier for the competition."
    )
    id_fight: str = Field(..., title="Fight ID", description="The unique identifier for the fight.")
    id_person_blue: str = Field(
        ..., title="Blue Person ID", description="The unique identifier for the blue competitor."
    )
    id_person_white: str = Field(
        ..., title="White Person ID", description="The unique identifier for the white competitor."
    )
    id_winner: str | None = Field(
        None, title="Winner ID", description="The unique identifier for the winner."
    )
    is_finished: bool = Field(
        ..., title="Is Finished", description="Indicates if the contest is finished."
    )
    round: int = Field(..., title="Round", description="The round number of the contest.")
    duration: str | None = Field(None, title="Duration", description="The duration of the contest.")
    gs: bool = Field(..., title="GS", description="Golden score.")
    bye: str = Field(..., title="Bye", description="Indicates if a bye was applied in the contest.")
    fight_duration: str | None = Field(
        None, title="Fight Duration", description="The duration of the fight."
    )
    weight: str | None = Field(
        None, title="Weight", description="The weight category or weight value."
    )
    id_weight: str | None = Field(
        None, title="Weight ID", description="The identifier for the weight category."
    )
    type: int = Field(..., title="Type", description="The type of contest.")
    round_code: str | None = Field(
        None, title="Round Code", description="The code representing the round."
    )
    round_name: str = Field(..., title="Round Name", description="The name of the round.")
    mat: int = Field(..., title="Mat", description="The mat number where the contest took place.")
    date_start_ts: datetime = Field(
        ..., title="Start Timestamp", description="The contest start timestamp."
    )
    updated_at: datetime = Field(
        ..., title="Updated At", description="The timestamp when the contest was last updated."
    )
    first_hajime_at_ts: datetime = Field(
        ...,
        title="First Hajime Timestamp",
        description="The timestamp of the first hajime (start signal).",
    )

    # White person details
    ippon_w: int | None = Field(
        None, title="White Ippon", description="Number of ippon scored by the white competitor."
    )
    waza_w: int | None = Field(
        None, title="White Waza", description="Number of waza-ari scored by the white competitor."
    )
    yuko_w: int | None = Field(
        None, title="White Yuko", description="Number of yuko scored by the white competitor."
    )
    penalty_w: int | None = Field(
        None,
        title="White Penalty",
        description="Number of penalties incurred by the white competitor.",
    )
    hsk_w: int | None = Field(
        None, title="White HSK", description="HSK score for the white competitor."
    )
    person_white: str = Field(
        ..., title="White Competitor", description="Name or identifier for the white competitor."
    )
    id_ijf_white: str = Field(
        ..., title="White IJF ID", description="The IJF ID for the white competitor."
    )
    family_name_white: str = Field(
        ..., title="White Family Name", description="Family name of the white competitor."
    )
    given_name_white: str = Field(
        ..., title="White Given Name", description="Given name of the white competitor."
    )
    timestamp_version_white: str = Field(
        ...,
        title="White Timestamp Version",
        description="Timestamp version for the white competitor record.",
    )
    country_white: str | None = Field(
        None, title="White Country", description="Country of the white competitor."
    )
    country_short_white: str | None = Field(
        None,
        title="White Country Short",
        description="Short country code for the white competitor.",
    )
    id_country_white: str | None = Field(
        None, title="White Country ID", description="Identifier for the white competitor's country."
    )
    picture_folder_1: str | None = Field(
        None,
        title="White Picture Folder",
        description="Folder path for the white competitor's picture.",
    )
    picture_filename_1: str | None = Field(
        None,
        title="White Picture Filename",
        description="Filename for the white competitor's picture.",
    )
    personal_picture_white: str | None = Field(
        None,
        title="White Personal Picture",
        description="URL or path to the white competitor's personal picture.",
    )

    # Blue person details
    ippon_b: int | None = Field(
        None, title="Blue Ippon", description="Number of ippon scored by the blue competitor."
    )
    waza_b: int | None = Field(
        None, title="Blue Waza", description="Number of waza-ari scored by the blue competitor."
    )
    yuko_b: int | None = Field(
        None, title="Blue Yuko", description="Number of yuko scored by the blue competitor."
    )
    penalty_b: int | None = Field(
        None,
        title="Blue Penalty",
        description="Number of penalties incurred by the blue competitor.",
    )
    hsk_b: int | None = Field(
        None, title="Blue HSK", description="HSK score for the blue competitor."
    )
    person_blue: str = Field(
        ..., title="Blue Competitor", description="Name or identifier for the blue competitor."
    )
    id_ijf_blue: str = Field(
        ..., title="Blue IJF ID", description="The IJF ID for the blue competitor."
    )
    family_name_blue: str = Field(
        ..., title="Blue Family Name", description="Family name of the blue competitor."
    )
    given_name_blue: str = Field(
        ..., title="Blue Given Name", description="Given name of the blue competitor."
    )
    timestamp_version_blue: str = Field(
        ...,
        title="Blue Timestamp Version",
        description="Timestamp version for the blue competitor record.",
    )
    country_blue: str | None = Field(
        None, title="Blue Country", description="Country of the blue competitor."
    )
    country_short_blue: str | None = Field(
        None, title="Blue Country Short", description="Short country code for the blue competitor."
    )
    id_country_blue: str | None = Field(
        None, title="Blue Country ID", description="Identifier for the blue competitor's country."
    )
    picture_folder_2: str | None = Field(
        None,
        title="Blue Picture Folder",
        description="Folder path for the blue competitor's picture.",
    )
    picture_filename_2: str | None = Field(
        None,
        title="Blue Picture Filename",
        description="Filename for the blue competitor's picture.",
    )
    personal_picture_blue: str | None = Field(
        None,
        title="Blue Personal Picture",
        description="URL or path to the blue competitor's personal picture.",
    )

    # Competitions details
    competition_name: str = Field(
        ..., title="Competition Name", description="The name of the competition."
    )
    external_id: str = Field(
        ..., title="External ID", description="The external identifier for the competition."
    )
    city: str = Field(..., title="City", description="City where the competition is held.")
    age: str | None = Field(
        None, title="Age", description="Age category or related age information."
    )
    rank_name: str | None = Field(
        None, title="Rank Name", description="Ranking name associated with the competition."
    )
    competition_date: str = Field(
        ..., title="Competition Date", description="The date of the competition."
    )
    date_raw: str = Field(..., title="Raw Date", description="Raw date string of the competition.")
    comp_year: str = Field(
        ..., title="Competition Year", description="The year of the competition."
    )

    # Other details
    tagged: int = Field(..., title="Tagged", description="Tag indicator for the contest.")
    kodokan_tagged: int = Field(..., title="Kodokan Tagged", description="Kodokan tag indicator.")
    published: str = Field(..., title="Published", description="Publication status of the contest.")
    sc_countdown_offset: int = Field(
        ..., title="SC Countdown Offset", description="Offset for the countdown timer."
    )
    fight_no: int = Field(
        ..., title="Fight Number", description="The number of the fight within the contest."
    )
    contest_code_long: str = Field(
        ..., title="Contest Code Long", description="The long form of the contest code."
    )
    media: str | None = Field(
        None, title="Media", description="Media details related to the contest."
    )
    id_competition_teams: str | None = Field(
        None, title="Competition Teams ID", description="Identifier for competition teams."
    )
    id_fight_team: str | None = Field(
        None, title="Fight Team ID", description="Identifier for the fight team."
    )

    @field_validator("updated_at", mode="after")
    @classmethod
    def parse_updated_at(cls, value: datetime) -> datetime:
        """Converts the `updated_at` field to a datetime object with UTC timezone."""
        return value.replace(tzinfo=timezone.utc)

    @field_validator("date_start_ts", mode="after")
    @classmethod
    def parse_date_start_ts(cls, value: datetime) -> datetime:
        """Converts the `date_start_ts` field to a datetime object with UTC timezone."""
        return value.replace(tzinfo=timezone.utc)

    @field_validator("first_hajime_at_ts", mode="after")
    @classmethod
    def parse_first_hajime_at_ts(cls, value: datetime) -> datetime:
        """Converts the `first_hajime_at_ts` field to a datetime object with UTC timezone."""
        return value.replace(tzinfo=timezone.utc)


class Judoka(BaseModel):
    """Represents the data about a judoka provided by the judobase API."""

    family_name: str = Field(
        ..., title="Family Name", description="The family name (surname) of the judoka."
    )
    middle_name: str | None = Field(
        None, title="Middle Name", description="The middle name of the judoka, if available."
    )
    given_name: str = Field(
        ..., title="Given Name", description="The given name (first name) of the judoka."
    )
    family_name_local: str = Field(
        ..., title="Local Family Name", description="The local representation of the family name."
    )
    middle_name_local: str | None = Field(
        None, title="Local Middle Name", description="The local representation of the middle name."
    )
    given_name_local: str = Field(
        ..., title="Local Given Name", description="The local representation of the given name."
    )
    short_name: str | None = Field(
        None, title="Short Name", description="A short or abbreviated name for the judoka."
    )
    gender: str = Field(..., title="Gender", description="The gender of the judoka.")
    folder: str = Field(
        ..., title="Folder", description="The folder where the judoka's data or images are stored."
    )
    picture_filename: str = Field(
        ..., title="Picture Filename", description="The filename of the judoka's picture."
    )
    ftechique: str | None = Field(
        None,
        title="Ftechique",
        description="A field representing a specific technique associated with the judoka. "
        "(Verify field name if necessary.)",
    )
    side: str = Field(
        ..., title="Side", description="The side (e.g., left or right) that the judoka uses."
    )
    coach: str = Field(..., title="Coach", description="The coach of the judoka.")
    best_result: str = Field(
        ..., title="Best Result", description="The best competition result achieved by the judoka."
    )
    height: str = Field(..., title="Height", description="The height of the judoka.")
    birth_date: datetime = Field(
        ..., title="Birth Date", description="The birth date of the judoka."
    )
    country: str = Field(..., title="Country", description="The country the judoka represents.")
    id_country: str = Field(
        ..., title="Country ID", description="The identifier for the judoka's country."
    )
    country_short: str = Field(
        ..., title="Country Short Code", description="The short code for the judoka's country."
    )
    file_flag: str | None = Field(
        None, title="File Flag", description="A flag indicating file status, if applicable."
    )
    club: str | None = Field(
        None, title="Club", description="The club the judoka is affiliated with."
    )
    belt: str | None = Field(None, title="Belt", description="The belt rank of the judoka.")
    youtube_links: str | None = Field(
        None, title="YouTube Links", description="Links to YouTube videos related to the judoka."
    )
    status: str | None = Field(
        None, title="Status", description="The current status of the judoka."
    )
    archived: str | None = Field(
        None, title="Archived", description="Indicates whether the judoka's record is archived."
    )
    categories: list[str] = Field(
        ...,
        title="Categories",
        description="List of competition categories the judoka participates in.",
    )
    dob_year: str | None = Field(
        None, title="Year of Birth", description="The year the judoka was born."
    )
    age: str | None = Field(None, title="Age", description="The age of the judoka.")
    death_age: str | None = Field(
        None,
        title="Death Age",
        description="The age at which the judoka passed away, if applicable.",
    )
    personal_picture: str = Field(
        ..., title="Personal Picture", description="URL or path to the judoka's personal picture."
    )

    @field_validator("birth_date", mode="after")
    @classmethod
    def parse_birth_date(cls, value: datetime) -> datetime:
        """Ensures the birth_date field is set to UTC timezone."""
        return value.replace(tzinfo=timezone.utc)


class Country(BaseModel):
    """Represents the data about a country provided by the Judobase API."""

    name: str = Field(..., title="Country Name", description="The full name of the country.")
    id_country: str = Field(
        ..., title="Country ID", description="The unique identifier for the country."
    )
    country_short: str = Field(
        ..., title="Country Short Code", description="The abbreviated country code."
    )
    org_name: str = Field(
        ..., title="Organization Name", description="The name of the national judo organization."
    )
    org_www: str = Field(
        ...,
        title="Organization Website",
        description="The website URL of the national organization.",
    )
    head_address: str = Field(
        ..., title="Head Address", description="The address of the organization's headquarters."
    )
    head_city: str = Field(
        ...,
        title="Head City",
        description="The city where the organization's headquarters are located.",
    )
    contact_phone: str = Field(
        ..., title="Contact Phone", description="The contact phone number for the organization."
    )
    contact_email: str = Field(
        ..., title="Contact Email", description="The contact email address for the organization."
    )
    exclude_from_medals: str = Field(
        ...,
        title="Exclude from Medals",
        description="Indicator if the country is excluded from medal counts.",
    )
    president_name: str = Field(
        ...,
        title="President Name",
        description="The name of the president of the national judo organization.",
    )
    male_competitiors: str = Field(
        ...,
        title="Male Competitors",
        description="Number of male competitors from the country. "
        "(Note: Field name may contain a typo.)",
    )
    female_competitiors: str = Field(
        ...,
        title="Female Competitors",
        description="Number of female competitors from the country. "
        "(Note: Field name may contain a typo.)",
    )
    total_competitors: int = Field(
        ...,
        title="Total Competitors",
        description="The total number of competitors representing the country.",
    )
    number_of_competitions: str = Field(
        ...,
        title="Number of Competitions",
        description="The number of competitions in which the country participated.",
    )
    number_of_total_competitions: str = Field(
        ...,
        title="Total Competitions",
        description="The total number of competitions involving the country.",
    )
    number_of_total_wins: int = Field(
        ...,
        title="Total Wins",
        description="The total number of wins achieved by competitors from the country.",
    )
    number_of_total_fights: int = Field(
        ...,
        title="Total Fights",
        description="The total number of fights involving competitors from the country.",
    )
    best_male_competitor: dict[str, Any] | None = Field(
        None,
        title="Best Male Competitor",
        description="Details of the best performing male competitor from the country.",
    )
    best_female_competitor: dict[str, Any] | None = Field(
        None,
        title="Best Female Competitor",
        description="Details of the best performing female competitor from the country.",
    )
    total_ranking_points: str | None = Field(
        None,
        title="Total Ranking Points",
        description="The total ranking points accumulated by the country.",
    )
    ranking: dict[str, Any] | None = Field(
        None, title="Overall Ranking", description="Overall ranking details for the country."
    )
    ranking_male: dict[str, Any] | None = Field(
        None,
        title="Male Ranking",
        description="Ranking details for male competitors from the country.",
    )
    ranking_female: dict[str, Any] | None = Field(
        None,
        title="Female Ranking",
        description="Ranking details for female competitors from the country.",
    )
