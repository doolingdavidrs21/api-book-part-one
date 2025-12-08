# SportsWorldCentral (SWC) Fantasy Football API Documenation

Thanks for using the SportsWorldCentral API. This is your one-stop shop for
accessing data from our fantasy football webiste, www.Sportsworldcentral.com.


## Table of Contents

- [Public API](#public-api)
- [Getting Started](#getting-started)
  - [Analytics](#analytics)
  - [Player](#player)
  - [Scoring](#scoring)
  - [Membership](#membership)
- [Terms of Service](#terms-of-service)
- [Example Code](#example-code)
- [Software Development Kit (SDK)](#software-development-kit-sdk)


## Public API
*Coming Soon*

Our API is hosted at [https://aws-api-container.xnkp6vj8k4sar.us-west-2.cs.amazonlightsail.com/](https://aws-api-container.xnkp6vj8k4sar.us-west-2.cs.amazonlightsail.com/). You can access the interactive documentation at [https://aws-api-container.xnkp6vj8k4sar.us-west-2.cs.amazonlightsail.com/docs](https://aws-api-container.xnkp6vj8k4sar.us-west-2.cs.amazonlightsail.com/docs)

You can view the OpenAPI Specification (OAS) file at
[https://aws-api-container.xnkp6vj8k4sar.us-west-2.cs.amazonlightsail.com/openapi.json](https://aws-api-container.xnkp6vj8k4sar.us-west-2.cs.amazonlightsail.com/openapi.json)

## Getting Started

Since all of the data is public, the SWC API doesn't require any authentication.
All of the following data is available using GET endpoints that return
JSON data.


### Analytics

Get information about the health of the API and counts of leagues, teams,
and players.

### Player

You can get a list of all NFL players, or search for an individual player
by player_id.

### Scoring

You can get a list of NFL player performances, including the fantasy points they
scored using SWC league scoring.


### Membership
Get information about all the SWC fantasy football leagues and the teams in them.

## Terms of Service

By using the API, you agree to the following terms of service:

- **Usage Limits**: You are allowed up to 2000 requests per day. Exceeding this
                    limit may result in your API key being suspended.
- **No Warranty**: We don't provide any warranty of the API or its operation.

## Example Code

The API is built using FastAPI and provides various endpoints for accessing fantasy football data. Here's a sample endpoint that demonstrates the API's capabilities:

```python
@app.get(
    "/v0/players/",
    response_model=list[schemas.Player],
    summary="Get all the SWC players that meet all the parameters you sent with your request",
    tags=["players"],
)
def read_players(
    skip: int = Query(0),
    limit: int = Query(100),
    first_name: str = Query(None),
    last_name: str = Query(None),
    db: Session = Depends(get_db),
):
    players = crud.get_players(
        db,
        skip=skip,
        limit=limit,
        first_name=first_name,
        last_name=last_name,
    )
    return players
```

This endpoint demonstrates several key features:
- Query parameter validation using FastAPI's `Query`
- Database integration using SQLAlchemy sessions
- Pagination support through `skip` and `limit` parameters
- Optional filtering by player names
- Automatic response serialization using Pydantic models
- OpenAPI documentation generation with descriptive tags

To use this endpoint, you can make a GET request like:
```bash
curl "http://localhost:8000/v0/players/?limit=5&first_name=Tom"
```

## Software Development Kit (SD)
*Coming Soon*

Check back for the Python SDK for our API.