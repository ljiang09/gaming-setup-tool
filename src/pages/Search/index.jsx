import { React, useEffect, useState } from "react";
import { Button, Box } from "@mui/material";

/**
 * A page for users to search for items in the database.
 * @returns {JSX.Element} A React component rendering the search input field.
 */
const Search = () => {
  const [imgFile, setImgFile] = useState(null);
  const [imgPreview, setImgPreview] = useState(null);
  const [color, setColor] = useState(null);

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

  const classifyImage = async () => {
    // TODO: replace these consts as needed
    const apiUrl = "http://127.0.0.1:5000/classifyImage";
    const data = { imgData: imgPreview };

    try {
      const response = await fetch(apiUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      const result = await response.json();
      window.alert(result.result);
    } catch (error) {
      window.alert(error);
      console.error("Error:", error);
    }
  };

  const getColors = async () => {
    // TODO: replace these consts as needed
    const apiUrl = "http://127.0.0.1:5000/getColors";
    const data = { imgData: imgPreview };

    try {
      const response = await fetch(apiUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      const result = await response.json();
      setColor(result.result);
      // window.alert(result.result);
    } catch (error) {
      window.alert(error);
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
      <Box
        height={300}
        style={{
          margin: "auto",
          marginTop: "20px",
          marginBottom: "20px",
        }}
      >
        {imgPreview ? (
          <img
            src={imgPreview}
            alt="preview"
            style={{
              maxWidth: "100%",
              maxHeight: "100%",
              width: "auto",
              height: "auto",
            }}
          />
        ) : (
          <div
            style={{
              height: "100%",
              aspectRatio: 1,
              background: "gray",
              margin: "auto",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              color: "white",
              fontSize: 24,
            }}
          >
            preview image here
          </div>
        )}
      </Box>

      <section
        style={{
          display: "flex",
          flexDirection: "row",
          gap: "20px",
          justifyContent: "center",
        }}
      >
        <Button
          variant="outlined"
          disabled={!imgPreview}
          onClick={classifyImage}
        >
          Predict
        </Button>
        <Button variant="outlined" disabled={!imgPreview} onClick={getColors}>
          Get Colors
        </Button>
      </section>

      {color && (
        <section
          style={{
            display: "flex",
            gap: "20px",
            alignItems: "center",
            justifyContent: "center",
            margin: "20px",
          }}
        >
          <div
            style={{
              width: "200px",
              height: "100px",
              backgroundColor: `rgba(${color})`,
              color: "white",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
            }}
          >
            {color[0]}, {color[1]}, {color[2]}
          </div>
          <div
            style={{
              width: "200px",
              height: "100px",
              backgroundColor: `rgba(${color})`,
              color: "black",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
            }}
          >
            {color[0]}, {color[1]}, {color[2]}
          </div>
        </section>
      )}
    </>
  );
};

export default Search;
