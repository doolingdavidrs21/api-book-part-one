import os
from dotenv import load_dotenv


load_dotenv()


class SWCConfig:
    """Configuration class containing arguments for the SDK client.
    Contains configuration for the base URL and progressive backoff."""

    swc_base_url: str
    swc_backoff: bool
    swc_backoff_max_time: int
    swc_bulk_file_format: str

    def __init__(
        self,
        swc_base_url: str = None,
        backoff: bool = True,
        backoff_max_time: int = 30,
        bulk_file_format: str = "csv",
    ):
        """Constructor for the SWCConfig class.
        Contains initialization values to overwrite defaults

        Args:
            swc_base_url (optional str): Base URL for the API
            backoff (bool): Enable progressive backoff
            backoff_max_time (int): The max number of seconds the SDK
                should keep trying an API call before stopping
            bulk_file_format (str): File format for bulk uploads,
                csv or parquet format
        """

        self.swc_base_url = swc_base_url or os.getenv("SWC_BASE_URL")
        print(f"SWC_API_BASE_URL in SWCConfig init: {self.swc_base_url}")

        if not self.swc_base_url:
            raise ValueError("""SWC_BASE_URL is required.
                              Set SWC_API_BASE_URL in .env""")
        self.swc_backoff = backoff
        self.swc_backoff_max_time = backoff_max_time
        self.swc_bulk_file_format = bulk_file_format

    def __str__(self):
        """Stringify function to return contents
        of config object for logging"""
        return f"""{self.swc_base_url}, {self.swc_backoff},
          {self.swc_backoff_max_time}, {self.swc_bulk_file_format}"""
