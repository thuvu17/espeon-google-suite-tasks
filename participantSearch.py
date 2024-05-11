from google.apps import meet_v2

#List all participant in the meeting
async def list_participants():
    # Create a client
    client = meet_v2.ConferenceRecordsServiceAsyncClient()

    # Initialize request argument(s)
    request = meet_v2.ListParticipantsRequest(
        parent="parent_value",
    )

    # Make the request
    page_result = client.list_participants(request=request)

    # Handle the response
    async for response in page_result:
        print(response)
#Search for a specific participant
async def get_participant():
    # Create a client
    client = meet_v2.ConferenceRecordsServiceAsyncClient()

    # Initialize request argument(s)
    request = meet_v2.GetParticipantRequest(
        name="name_value",
    )

    # Make the request
    response = await client.get_participant(request=request)

    # Handle the response
    print(response)
