import Link from 'next/link';
import { AppBar, Toolbar, Typography, Button, Box } from '@mui/material';
import { Home, Receipt, Person, CloudUpload } from '@mui/icons-material'; // Make sure these icons are installed: npm install @mui/icons-material

export default function Navigation() {
  return (
    <AppBar position="static" color="primary">
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          SmartSpend Analyzer
        </Typography>
        <Box sx={{ display: { xs: 'none', sm: 'block' } }}>
          <Link href="/" passHref>
            <Button color="inherit" startIcon={<Home />}>
              Dashboard
            </Button>
          </Link>
          <Link href="/upload" passHref>
            <Button color="inherit" startIcon={<CloudUpload />}>
              Upload
            </Button>
          </Link>
          <Link href="/profile" passHref>
            <Button color="inherit" startIcon={<Person />}>
              Profile
            </Button>
          </Link>
        </Box>
      </Toolbar>
    </AppBar>
  );
}