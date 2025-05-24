import Layout from '../components/Layout';
import { Box, Grid, Paper, Typography } from '@mui/material';
import { BarChart, PieChart } from '../components/Charts';
import RecentTransactions from '../components/RecentTransactions';
import SpendingSummary from '../components/SpendingSummary';

export default function Dashboard() {
  return (
    <Layout>
      <Typography variant="h4" gutterBottom>
        Dashboard
      </Typography>
      
      <Grid container spacing={3}>
        <Grid item xs={12} md={8}>
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" gutterBottom>
              Monthly Spending
            </Typography>
            <BarChart />
          </Paper>
        </Grid>
        
        <Grid item xs={12} md={4}>
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" gutterBottom>
              Spending Categories
            </Typography>
            <PieChart />
          </Paper>
        </Grid>
        
        <Grid item xs={12} md={6}>
          <Paper sx={{ p: 2 }}>
            <SpendingSummary />
          </Paper>
        </Grid>
        
        <Grid item xs={12} md={6}>
          <Paper sx={{ p: 2 }}>
            <RecentTransactions />
          </Paper>
        </Grid>
      </Grid>
    </Layout>
  );
}