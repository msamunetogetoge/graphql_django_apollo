import "./App.css";

import { ApolloProvider } from "@apollo/client";
import client from "./apolloClient";
import EmployeeList from "./EmployeeList";
import EmployeeFilteredList from "./EmployeeFilteredList";

function App() {
  return (
    <ApolloProvider client={client}>
      <div className="App">
        <EmployeeFilteredList />
      </div>
    </ApolloProvider>
  );
}

export default App;
