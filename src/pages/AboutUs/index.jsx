import { Grid, Typography } from "@mui/material";

/**
 * A page detailing the creators of the app.
 * @returns {JSX.Element} A React component rendering the About Us content.
 */
const AboutUs = () => {
  return (
    <Grid container style={{ marginTop: 30 }}>
      <Grid
        item
        xs={6}
        style={{
          display: "flex",
          flexDirection: "column",
          gap: 20,
          alignItems: "center",
        }}
      >
        <Typography variant="h4">Lily Jiang</Typography>
        <div style={{ background: "#D3D3D3", height: 200, width: 200 }}>
          Picture Here
        </div>
        <Typography variant="body1">Short Description Here</Typography>
      </Grid>
      <Grid
        item
        xs={6}
        style={{
          display: "flex",
          flexDirection: "column",
          gap: 20,
          alignItems: "center",
        }}
      >
        <Typography variant="h4">Aditi Vinod</Typography>
        <div style={{ background: "#D3D3D3", height: 200, width: 200 }}>
          Picture Here
        </div>
        <Typography variant="body1">Short Description Here</Typography>
      </Grid>
    </Grid>
  );
};

export default AboutUs;
