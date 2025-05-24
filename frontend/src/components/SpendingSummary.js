import { Box, Typography } from '@mui/material';

export default function SpendingSummary() {
  return (
    <>
      <Typography variant="h6" gutterBottom>
        Spending Summary
      </Typography>
      <Box sx={{ display: 'flex', justifyContent: 'space-between' }}>
        <Typography>This Month:</Typography>
        <Typography>$1,850.00</Typography>
      </Box>
      <Box sx={{ display: 'flex', justifyContent: 'space-between' }}>
        <Typography>Last Month:</Typography>
        <Typography>$2,100.00</Typography>
      </Box>
      <Box sx={{ display: 'flex', justifyContent: 'space-between' }}>
        <Typography>Average Daily:</Typography>
        <Typography>$61.67</Typography>
      </Box>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', mt: 2 }}>
        <Typography variant="subtitle1">Savings Rate:</Typography>
        <Typography variant="subtitle1" color="primary">
          15%
        </Typography>
      </Box>
    </>
  );
}