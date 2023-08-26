// src/EmployeeFilteredList.tsx
import React, { useState, useEffect } from "react";
import { useQuery } from "@apollo/client";
import {
  List,
  ListItem,
  ListItemText,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
} from "@mui/material";
import gql from "graphql-tag";

// 部署とプロジェクトのリストを取得するクエリ
const GET_FILTER_OPTIONS = gql`
  query GetFilterOptions {
    allDepartments {
      edges {
        node {
          id
          name
        }
      }
    }
    allProjects {
      edges {
        node {
          id
          name
        }
      }
    }
  }
`;

// 選択された部署とプロジェクトに関連する社員を取得するクエリ
const GET_EMPLOYEES_BY_FILTER = gql`
  query GetEmployeesByFilter($departmentId: ID!, $projectId: ID!) {
    employeesByDepartmentAndProject(
      departmentId: $departmentId
      projectId: $projectId
    ) {
      id
      name
    }
  }
`;

function EmployeeFilteredList() {
  const {
    loading: optionsLoading,
    error: optionsError,
    data: optionsData,
  } = useQuery(GET_FILTER_OPTIONS);

  const [selectedDepartment, setSelectedDepartment] = useState<string>("");
  const [selectedProject, setSelectedProject] = useState<string>("");

  useEffect(() => {
    console.log(selectedDepartment);
  }, [selectedDepartment]);

  const {
    loading: employeesLoading,
    error: employeesError,
    data: employeesData,
  } = useQuery(GET_EMPLOYEES_BY_FILTER, {
    variables: { departmentId: selectedDepartment, projectId: selectedProject },
    skip: !selectedDepartment || !selectedProject,
  });

  // 部署の選択をハンドル
  const handleDepartmentChange = (
    event: React.ChangeEvent<{ value: unknown }>
  ) => {
    console.log(event.target.value);
    setSelectedDepartment(event.target.value as string);
    console.log(selectedDepartment);
  };

  // プロジェクトの選択をハンドル
  const handleProjectChange = (
    event: React.ChangeEvent<{ value: unknown }>
  ) => {
    console.log(event.target.value);
    setSelectedProject(event.target.value as string);
    console.log(selectedProject);
  };

  if (optionsLoading || employeesLoading) return <p>Loading...</p>;
  if (optionsError) {
    return <p>OPTIONS Error: {optionsError?.message}</p>;
  }
  if (employeesError)
    return (
      <p>
        EMPLOYEE Error: data= {selectedDepartment}, {selectedProject},
        {employeesError?.message}
      </p>
    );
  if (employeesData) {
    console.log(employeesData);
  }
  return (
    <div>
      <FormControl fullWidth>
        <InputLabel>部署</InputLabel>
        <Select value={selectedDepartment} onChange={handleDepartmentChange}>
          {optionsData.allDepartments.edges.map((edge) => (
            <MenuItem key={edge.node.id} value={edge.node.id}>
              {edge.node.name}
            </MenuItem>
          ))}
        </Select>
      </FormControl>
      <FormControl fullWidth>
        <InputLabel>プロジェクト</InputLabel>
        <Select value={selectedProject} onChange={handleProjectChange}>
          {optionsData.allProjects.edges.map((edge) => (
            <MenuItem key={edge.node.id} value={edge.node.id}>
              {edge.node.name}
            </MenuItem>
          ))}
        </Select>
      </FormControl>
      <List>
        {employeesData?.employeesByDepartmentAndProject.map((edge) => (
          <ListItem key={edge.id}>
            <ListItemText primary={edge.name} />
          </ListItem>
        ))}
      </List>
    </div>
  );
}

export default EmployeeFilteredList;
