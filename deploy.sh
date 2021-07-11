#!/bin/bash
NODE_ENV=production npx next
netlify build
netlify deploy --prod
echo "Deployment complete"
