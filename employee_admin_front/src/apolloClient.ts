// src/apolloClient.ts
import { ApolloClient, InMemoryCache } from "@apollo/client";

const client = new ApolloClient({
  uri: "http://localhost:8000/graphql/", // DjangoでのGraphQLエンドポイントURLを指定
  //  uri: "https://flyby-router-demo.herokuapp.com/",
  cache: new InMemoryCache(),
});

export default client;
