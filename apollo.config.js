// apollo.config.js
module.exports = {
  client: {
    service: {
      name: "django_vue",
      // URL to the GraphQL API
      url: "http://0.0.0.0:8000/graphql",
    },

    // Files processed by the extension
    includes: [
      "frontend/src/**/*.vue",
      "frontend/src/**/*.js",
      "frontend/src/**/*.gql",
    ],
  },
};
