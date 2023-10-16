import { useState } from "react";
import { Tabs, Tab, Typography } from "@mui/material";
import { AboutUs, ImageDatabase, Search } from "./pages";
import "./App.css";

/**
 * The root page content.
 * @returns {JSX.Element} A React component rendering the website.
 */
function App() {
  const [tabValue, setTabValue] = useState(0);

  const handleTabChange = (event, newTab) => {
    setTabValue(newTab);
  };

  return (
    <div className="App">
      <Typography style={{ marginTop: "20px", fontSize: "30px" }}>
        Gaming Setup Finder
      </Typography>

      <Tabs value={tabValue} onChange={handleTabChange}>
        <Tab label="Search" />
        <Tab label="Image Database" />
        <Tab label="About Us" />
      </Tabs>

      {tabValue === 0 && <Search />}
      {tabValue === 1 && <ImageDatabase />}
      {tabValue === 2 && <AboutUs />}
    </div>
  );
}

export default App;
