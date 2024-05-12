from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.apps import meet_v2

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/meetings.space.created"]


def get_token():
    """Shows basic usage of the Google Meet API."""
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file
            ("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0, success_message="认证成功")
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return creds


##############################################################################
# meeting spaces
##############################################################################
# Create Meeting Space
async def sample_create_space():
    # Create a client
    client = meet_v2.SpacesServiceAsyncClient(credentials=get_token())

    # Initialize request argument(s)
    request = meet_v2.CreateSpaceRequest()

    # Make the request
    response = await client.create_space(request=request)

    return response


# Get Meeting Space
async def sample_get_space(name):
    # Create a client
    client = meet_v2.SpacesServiceAsyncClient(credentials=get_token())

    # Initialize request argument(s)
    request = meet_v2.GetSpaceRequest(
        name=name,
    )

    # Make the request
    response = await client.get_space(request=request)

    # Handle the response
    return response


# Update Meeting Space
async def sample_update_space(name):
    # Create a client
    client = meet_v2.SpacesServiceAsyncClient(credentials=get_token())

    # Initialize request argument(s)
    request = meet_v2.UpdateSpaceRequest(
        {
            "space": {
                "name": name,
            },
            "update_mask": {},
        },
    )

    # Make the request
    response = await client.update_space(request=request)

    # Handle the response
    return response


# End Meeting
async def sample_end_active_conference(name):
    # Create a client
    client = meet_v2.SpacesServiceAsyncClient(credentials=get_token())

    # Initialize request argument(s)
    request = meet_v2.EndActiveConferenceRequest(
        name=name,
    )

    # Make the request
    await client.end_active_conference(request=request)


##############################################################################
# conferences
##############################################################################
# Search All Meetings
async def sample_list_conference_records():
    # Create a client
    client = meet_v2.ConferenceRecordsServiceAsyncClient(credentials=get_token())

    # Initialize request argument(s)
    request = meet_v2.ListConferenceRecordsRequest()

    # Make the request
    page_result = await client.list_conference_records(request=request)

    return page_result

    # Handle the response
    # result_lines = []
    # async for response in page_result:
    #     result_lines.append(response)
    #     # print(response)
    # return '\n'.join(result_lines)


# Search Specific Meeting
async def sample_get_conference_record(name):
    # Create a client
    client = meet_v2.ConferenceRecordsServiceAsyncClient(credentials=get_token())

    # Initialize request argument(s)
    request = meet_v2.GetConferenceRecordRequest(
        name=name,
    )

    # Make the request
    response = await client.get_conference_record(request=request)

    # Handle the response
    return response


#######################################################################################
# participants
#######################################################################################
# Search All Particpants
async def sample_list_participants(name):
    # Create a client
    client = meet_v2.ConferenceRecordsServiceAsyncClient(credentials=get_token())

    # Initialize request argument(s)
    request = meet_v2.ListParticipantsRequest(
        parent=name,
    )

    # Make the request
    page_result = await client.list_participants(request=request)

    # Handle the response
    return page_result
    # async for response in page_result:
    #     print(response)


# Search Specific Participants
async def sample_get_participant(name):
    # Create a client
    client = meet_v2.ConferenceRecordsServiceAsyncClient(credentials=get_token())

    # Initialize request argument(s)
    request = meet_v2.GetParticipantRequest(
        name=name,
    )

    # Make the request
    response = await client.get_participant(request=request)

    # Handle the response hy
    return response


async def sample_list_participant_sessions(name):
    # Create a client
    client = meet_v2.ConferenceRecordsServiceAsyncClient(credentials=get_token())

    # Initialize request argument(s)
    request = meet_v2.ListParticipantSessionsRequest(parent=name)

    # Make the request
    page_result = await client.list_participant_sessions(request=request)

    # Handle the response
    return page_result
    # async for response in page_result:
    #     print(response)


async def sample_get_participant_session(name):
    # Create a client
    client = meet_v2.ConferenceRecordsServiceAsyncClient(credentials=get_token())

    # Initialize request argument(s)
    request = meet_v2.GetParticipantSessionRequest(name=name)

    # Make the request
    response = await client.get_participant_session(request=request)

    # Handle the response
    return response
