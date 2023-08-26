// src/EmployeeList.tsx
import { useQuery } from "@apollo/client";
import { List, ListItem, ListItemText } from "@mui/material";
import gql from "graphql-tag";

const GET_EMPLOYEES = gql`
  query GetEmployees {
    allEmployees {
      edges {
        node {
          id
          name
          department {
            name
          }
        }
      }
    }
  }
`;

function EmployeeList() {
  const { loading, error, data } = useQuery(GET_EMPLOYEES);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error.message}</p>;

  return (
    <List>
      {data.allEmployees.edges.map((edge) => (
        <ListItem key={edge.node.id}>
          <ListItemText
            primary={edge.node.name}
            secondary={edge.node.department.name}
          />
        </ListItem>
      ))}
    </List>
  );
}

export default EmployeeList;
