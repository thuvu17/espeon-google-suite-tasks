from google.apps import meet_v2

async def sample_create_space():
    # Create a client
    client = meet_v2.SpacesServiceAsyncClient()

    # Initialize request argument(s)
    request = meet_v2.CreateSpaceRequest(
    )

    # Make the request
    response = await client.create_space(request=request)

    # Handle the response
    print(response)

async def sample_get_space():
    # Create a client
    client = meet_v2.SpacesServiceAsyncClient()

    # Initialize request argument(s)
    request = meet_v2.GetSpaceRequest(
        name="name_value",
    )

    # Make the request
    response = await client.get_space(request=request)

    # Handle the response
    print(response)

async def sample_update_space():
    # Create a client
    client = meet_v2.SpacesServiceAsyncClient()

    # Initialize request argument(s)
    request = meet_v2.UpdateSpaceRequest(
    )

    # Make the request
    response = await client.update_space(request=request)

    # Handle the response
    print(response)

async def sample_end_active_conference():
    # Create a client
    client = meet_v2.SpacesServiceAsyncClient()

    # Initialize request argument(s)
    request = meet_v2.EndActiveConferenceRequest(
        name="name_value",
    )

    # Make the request
    await client.end_active_conference(request=request)
