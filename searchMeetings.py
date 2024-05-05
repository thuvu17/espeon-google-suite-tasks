from google.apps import meet_v2

# Search for all meetings
async def sample_list_conference_records():
    # Create a client
    client = meet_v2.ConferenceRecordsServiceAsyncClient()

    # Initialize request argument(s)
    request = meet_v2.ListConferenceRecordsRequest(
    )

    # Make the request
    page_result = client.list_conference_records(request=request)

    # Handle the response
    async for response in page_result:
        print(response)

#Search for one specific meeting
async def sample_get_conference_record():
    # Create a client
    client = meet_v2.ConferenceRecordsServiceAsyncClient()

    # Initialize request argument(s)
    request = meet_v2.GetConferenceRecordRequest(
        name="name_value",
    )

    # Make the request
    response = await client.get_conference_record(request=request)

    # Handle the response
    print(response)
