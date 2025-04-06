#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

"""Storage service versions command"""

import click

from osducli.click_cli import CustomClickCommand, State, global_params
from osducli.cliclient import CliOsduClient, handle_cli_exceptions
from osducli.config import CONFIG_STORAGE_URL


# click entry point
@click.command(cls=CustomClickCommand)
@click.option("-id", "--id", "_id", required=True, help="id to delete")
@handle_cli_exceptions
@global_params
def _click_command(state: State, _id: str):
    """Delete records"""
    return delete(state, _id)


def delete(state: State, id: str):  # pylint: disable=invalid-name,redefined-builtin
    """Delete records

    Args:
        state (State): Global state
        id (str): id to delete
    """
    connection = CliOsduClient(state.config)
    url = "records/" + id
    connection.cli_delete(CONFIG_STORAGE_URL, url, [200, 204])

    if state.is_user_friendly_mode():
        print("1 record deleted")
