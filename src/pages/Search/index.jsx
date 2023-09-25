import { React, useEffect, useState } from "react";
import { Button, Box } from "@mui/material";

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
    </>
  );
};

export default Search;
