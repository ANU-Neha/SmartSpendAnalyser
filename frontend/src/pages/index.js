import Layout from '../components/Layout';
import { Grid, Paper, Typography, Box } from '@mui/material'; // Make sure to import Box
import { BarChart, PieChart } from '../components/Charts';
import ReactTransactions from '../components/ReactTransactions';
import SpendingSummary from '../components/SpendingSummary';

export default function Dashboard() {
  return (
    <Layout>
      <Typography variant="h4" gutterBottom>
        Dashboard
      </Typography>

      <Grid container spacing={3}>
        <Grid item xs={12} md={8}>
          <Paper
            sx={{
              p: 2,
              display: 'flex', // Use flexbox for internal layout
              flexDirection: 'column', // Stack children vertically
              height: '100%', // Allow Paper to fill parent Grid item's height
              maxHeight: { xs: 'none', md: '400px' }, // Set a max height for the chart container
              overflowY: 'auto', // Enable vertical scrolling if chart content exceeds maxHeight
            }}
          >
            <Typography variant="h6" gutterBottom>
              Monthly Spending
            </Typography>
            {/* Wrap BarChart in a Box to ensure Chart.js has a constrained height */}
            <Box sx={{ flexGrow: 1, position: 'relative', height: '100%' }}>
              <BarChart />
            </Box>
          </Paper>
        </Grid>

        <Grid item xs={12} md={4}>
          <Paper
            sx={{
              p: 2,
              display: 'flex', // Use flexbox for internal layout
              flexDirection: 'column', // Stack children vertically
              height: '100%', // Allow Paper to fill parent Grid item's height
              maxHeight: { xs: 'none', md: '400px' }, // Set a max height for the chart container
              overflowY: 'auto', // Enable vertical scrolling if chart content exceeds maxHeight
            }}
          >
            <Typography variant="h6" gutterBottom>
              Spending Categories
            </Typography>
            {/* Wrap PieChart in a Box to ensure Chart.js has a constrained height */}
            <Box sx={{ flexGrow: 1, position: 'relative', height: '100%' }}>
              <PieChart />
            </Box>
          </Paper>
        </Grid>

        <Grid item xs={12} md={6}>
          <Paper sx={{ p: 2 }}>
            <SpendingSummary />
          </Paper>
        </Grid>

        {/* This is the ReactTransactions Paper - your existing modifications are kept */}
        <Grid item xs={12} md={6}>
          <Paper
            sx={{
              p: 2,
              display: 'flex', // Use flexbox for internal layout
              flexDirection: 'column', // Stack children vertically
              height: '100%', // Take full height of parent Grid item (if parent has height)
              maxHeight: { xs: 'none', md: '400px' }, // Set a max height (e.g., 400px, adjust as needed)
              overflowY: 'auto', // Enable vertical scrolling if content exceeds maxHeight
              // overflowX: 'hidden', // Hide horizontal scroll if not needed
            }}
          >
            <ReactTransactions />
          </Paper>
        </Grid>
      </Grid>
    </Layout>
  );
}