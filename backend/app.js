const dialogflow = require("@google-cloud/dialogflow");
const uuid = require("uuid");
const express = require("express");
const bodyParser = require("body-parser");
const serverless = require("serverless-http");

const app = express();
// const router = express.Router();
const port = 5000;

// A unique identifier for the given session
const sessionId = uuid.v4();

app.use(
  bodyParser.urlencoded({
    extended: false,
  })
);

app.use(function (req, res, next) {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader(
    "Access-Control-Allow-Methods",
    "GET, POST, OPTIONS, PUT, PATCH, DELETE"
  );
  res.setHeader(
    "Access-Control-Allow-Headers",
    "X-Requested-With,content-type"
  );
  res.setHeader("Access-Control-Allow-Credentials", true);

  // Pass to next layer of middleware
  next();
});

app.post("/send-msg", (req, res) => {
  runSample(req.body.MSG).then((data) => {
    res.send({ Reply: data });
  });
});

async function runSample(msg, projectId = "chatbot-dialogflow-xxnp") {
  // Create a new session
  const sessionClient = new dialogflow.SessionsClient({
    keyFilename: "/backend/chatbot-dialogflow-xxnp-521037ab179b.json",
  });
  const sessionPath = sessionClient.projectAgentSessionPath(
    projectId,
    sessionId
  );

  // The text query request.
  const request = {
    session: sessionPath,
    queryInput: {
      text: {
        text: msg,
        languageCode: "en-US",
      },
    },
  };

  // Send request and log result
  const responses = await sessionClient.detectIntent(request);
  // console.log("Detected intent");
  const result = responses[0].queryResult;
  console.log(`  Query: ${result.queryText}`);

  const parameters = result.parameters;
  // const curiousEntity = parameters["curious-entity"].stringValue;
  // console.log(`  Parameters: ${curiousEntity}`);
  console.log(`  Parameters:`, parameters);

  // console.log(`  Intent: ${result.intent.displayName}`);
  // console.log(`  Entity: ${result.entity}`);
  // console.log(`  Parameters: ${result.parameter.original}`);

  console.log(`  Response: ${result.fulfillmentText}`);
  if (result.intent) {
    console.log(`  Intent: ${result.intent.displayName}`);
  } else {
    console.log("  No intent matched.");
  }

  return result.fulfillmentText;
}

app.listen(port, () => {
  console.log("Running server on port 5000");
});
