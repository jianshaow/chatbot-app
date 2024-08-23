import { createOpenAI } from '@ai-sdk/openai';
import { streamText, convertToCoreMessages } from 'ai';

const openai = createOpenAI({
    apiKey: process.env.OPENAI_API_KEY || '',
    baseURL: process.env.OPENAI_BASE_URL || "https://api.openai-proxy.com/v1"
});

export const maxDuration = 30;

export async function POST(req: Request) {
    const { messages } = await req.json();

    const result = await streamText({
        model: openai('gpt-4o-mini'),
        messages: convertToCoreMessages(messages),
    });

    return result.toDataStreamResponse();
}
