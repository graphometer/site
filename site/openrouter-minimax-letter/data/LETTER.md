# The letter, as received

Received by the Graphometer account holder on 21 November 2026, by email, from OpenRouter.
Transcribed exactly from the image of the email as received (`openrouter-letter-2026-11-21.png`, beside the page,
542 by 877 pixels, sha256 `0f44e57738d0c8eeed63d636f069580a0b2a045aff1d48ec4a9687b7c6e5aa1f`).
The email shows no recipient name or address. Its heading is the bold line below. Line breaks within paragraphs are
the email's layout and are not kept. The one button is shown in square brackets. The underlined
address in the last paragraph is a link in the email.

---

openrouter

**Requests you sent to MiniMax models may have been read**

Hi there,

A security researcher placed unique test URLs in prompts sent to MiniMax models from July to October 2026. A third party accessed those URLs 40 to 130 hours after the requests were sent, whether MiniMax served a request directly or another provider forwarded it to MiniMax. With one exception, the same tests on other models at those providers were not accessed, and none of the AWS test keys were used.

Your account sent 7,619 requests to MiniMax models through MiniMax, from August 24 at 01:07 to October 8 at 22:36 UTC.

AtlasCloud, Novita and StreamLake have told us they forwarded OpenRouter requests for MiniMax models to MiniMax. Based on what the researcher and these providers have reported, the issue sits with MiniMax and the providers that forwarded to it, not with OpenRouter. We are passing on what they have told us. MiniMax told StreamLake that content moderation was enabled on its endpoints before October 22 and that it has since enabled Zero Data Retention. We have asked MiniMax for its own account and have not received one.

This means a third party may have read the prompts and outputs of these requests. While we investigate, we have removed the Zero Data Retention label from these MiniMax-model endpoints.

[Review your activity]

Rotate any keys, passwords, tokens or signed URLs that appeared in those prompts or outputs, starting with the most privileged.

We will email you again if MiniMax's or the providers' findings change this notice. For questions, contact support@openrouter.ai.

The OpenRouter Team
