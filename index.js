const express = require("express");
require("dotenv").config();

const app = express();
app.use(express.json());

//Old
// const { Configuration, OpenAIApi } = require("openai");

// const configuration = new Configuration({
//     apiKey: process.env.OPEN_API_KEY,
// });
// const openai = new OpenAIApi(configuration);

//New
const OpenAI = require("openai");

const openai = new OpenAI({
  apiKey: process.env.OPEN_AI_KEY
});

app.post("/find-complexity", async (req, res) => {
    try {
        // const { prompt } = req.body;
        const response = await openai.completions.create({
            model: "text-davinci-003",
            prompt: `
                
            van_id,visit_date,outlet_id,lng,lat,check_in_at,check_out_at,travelled_time
            V2XV001,1/7/2023,21101013,100.71856,4.85454,2023-07-01 12:05:25.000 +0800,2023-07-01 12:06:57.924 +0800,02:34.1
            V2XV001,4/7/2023,21110043,100.74137,4.84993,2023-07-04 17:00:57.000 +0800,2023-07-04 17:03:41.550 +0800,02:09.6
            V2XV001,3/7/2023,349751,100.72426,4.84123,2023-07-03 08:48:37.000 +0800,2023-07-03 17:02:43.514 +0800,07:52.5
            V2XV001,4/7/2023,698148,100.73873,4.85025,2023-07-04 16:59:44.000 +0800,2023-07-04 17:03:54.591 +0800,04:04.6
            V2XV001,3/7/2023,594670,100.74109,4.8508,2023-07-03 17:04:18.000 +0800,2023-07-03 17:05:49.854 +0800,01:23.9
            V2XV001,4/7/2023,739071,100.74296,4.85025,2023-07-04 08:51:23.000 +0800,2023-07-04 09:58:31.858 +0800,06:34.9
            V2XV001,1/7/2023,21108050,100.71282,4.85297,2023-07-01 11:35:18.000 +0800,2023-07-01 11:35:43.702 +0800,05:16.3


            Generate a python code that will plot a coordinate graph by using the "lng" as y-axis, and "lat" as x-axis.
                ###`
            ,
            // prompt: `
            //     const example = (arr) => {
            //         arr.map((item) => {
            //             console.log(item2);
            //         });
            //     };

            //     The time commplexity of this function is
            //     ###
            // `,

            max_tokens: 2000,
            temperature: 1,
            // stop: ["\n"],
        });

        console.log("Output data:", response);

        const generatedText = response.choices[0].text;
        console.log("Generated Text:", generatedText);

        return res.status(200).json({
            success: true,
            data: response.choices[0].text,
            message: "Working.",
        });
    } catch (error) {
        
        return res.status(400).json({
            success: false,
            error: error instanceof OpenAI.APIError
                ? error.message
                : "There was an issue on the server."
        })
    }
});

const port = process.env.PORT || 5000;

app.listen(port, () => console.log(`Server listening on port ${port}`));