from fastapi import APIRouter, Request
import openai

router = APIRouter()

@router.post("/health/query")
async def health_query(request: Request):
    body = await request.json()
    user_input = body.get("query")

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful health assistant."},
            {"role": "user", "content": user_input}
        ]
    )

    return {"response": response.choices[0].message["content"]}