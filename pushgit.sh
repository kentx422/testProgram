#!/bin/bash
 
// make message from Git log
message=$(git log -1 --pretty=format:"%h - %an : %s" --branches)
 
// make payload
payload="payload={\"channel\": \"G0EEV0PF0\", \"username\": \"webhookbot\", \"text\": \"${message}\", \"icon_emoji\": \":ghost:\"}"
 
// POST to Slack
curl -X POST --data-urlencode "${payload}" https://hooks.slack.com/services/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
