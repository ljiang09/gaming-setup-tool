import { React, useEffect, useState } from "react";
import { Button, Box } from "@mui/material";

/**
 * A page for users to search for items in the database.
 * @returns {JSX.Element} A React component rendering the search input field.
 */
const Search = () => {
  const [imgFile, setImgFile] = useState(null);
  const [imgPreview, setImgPreview] = useState(null);

  const handleFileChange = (event) => {
    setImgFile(event.target.files[0]);
  };

  // store uploaded file as base64 to display
  useEffect(() => {
    if (imgFile) {
      const reader = new FileReader();
      reader.onload = () => {
        setImgPreview(reader.result);
      };
      reader.readAsDataURL(imgFile);
    } else {
      setImgPreview(null);
    }
  }, [imgFile]);

  const makeApiCall = async () => {
    // TODO: replace these consts as needed
    const apiUrl = "http://127.0.0.1:5000/hello";
    const data = { name: "Lily" };

    try {
      const response = await fetch(apiUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      const result = await response.json();
      window.alert(result.message);
      // console.log(result.message);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <>
      <Button variant="outlined" component="label">
        {imgFile ? "Edit Image" : "Upload Image"}
        <input
          type="file"
          accept="image/*"
          hidden
          onChange={handleFileChange}
        />
      </Button>
      <Box width={200} style={{ margin: "auto", marginTop: "20px" }}>
        {imgPreview && (
          <img
            src={imgPreview}
            alt="preview"
            style={{ width: "100%", height: "100%" }}
          />
        )}
      </Box>
      <Button onClick={makeApiCall}>erm</Button>
    </>
  );
};

export default Search;
