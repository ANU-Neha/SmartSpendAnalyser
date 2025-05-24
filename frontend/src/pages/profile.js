import Layout from '../components/Layout';
import { Avatar, Box, Typography, Paper, List, ListItem, ListItemText, Divider } from '@mui/material';
import { Person, Email, DateRange, AttachMoney } from '@mui/icons-material';

export default function Profile() {
  const user = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    joinDate: 'January 2023',
    totalSpent: 5840.50,
  };

  return (
    <Layout>
      <Typography variant="h4" gutterBottom>
        User Profile
      </Typography>
      
      <Paper sx={{ p: 3, mb: 3 }}>
        <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
          <Avatar sx={{ width: 80, height: 80, mr: 3, bgcolor: 'primary.main' }}>
            {user.name.charAt(0)}
          </Avatar>
          <Box>
            <Typography variant="h5">{user.name}</Typography>
            <Typography variant="body1" color="text.secondary">
              Member since {user.joinDate}
            </Typography>
          </Box>
        </Box>
        
        <Divider sx={{ my: 2 }} />
        
        <List>
          <ListItem>
            <Person color="primary" sx={{ mr: 2 }} />
            <ListItemText primary="Name" secondary={user.name} />
          </ListItem>
          <ListItem>
            <Email color="primary" sx={{ mr: 2 }} />
            <ListItemText primary="Email" secondary={user.email} />
          </ListItem>
          <ListItem>
            <DateRange color="primary" sx={{ mr: 2 }} />
            <ListItemText primary="Member Since" secondary={user.joinDate} />
          </ListItem>
          <ListItem>
            <AttachMoney color="primary" sx={{ mr: 2 }} />
            <ListItemText primary="Total Spent" secondary={`$${user.totalSpent.toFixed(2)}`} />
          </ListItem>
        </List>
      </Paper>
      
      <Typography variant="h5" gutterBottom>
        Account Settings
      </Typography>
      <Paper sx={{ p: 3 }}>
        {/* Add account settings form here */}
        <Typography>Coming soon...</Typography>
      </Paper>
    </Layout>
  );
}