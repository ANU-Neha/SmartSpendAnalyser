import { Table, TableBody, TableCell, TableHead, TableRow, Typography } from '@mui/material';

export default function ReactTransactions() {
  const transactions = [
    { id: 1, store: 'Grocery Store', amount: 85.50, date: '2023-05-15' },
    { id: 2, store: 'Gas Station', amount: 45.20, date: '2023-05-14' },
    { id: 3, store: 'Restaurant', amount: 32.75, date: '2023-05-13' },
    { id: 4, store: 'Online Shopping', amount: 120.00, date: '2023-05-12' },
  ];

  return (
    <>
      <Typography variant="h6" gutterBottom>
        Recent Transactions
      </Typography>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>Store</TableCell>
            <TableCell align="right">Amount</TableCell>
            <TableCell>Date</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {transactions.map((tx) => (
            <TableRow key={tx.id}>
              <TableCell>{tx.store}</TableCell>
              <TableCell align="right">${tx.amount.toFixed(2)}</TableCell>
              <TableCell>{tx.date}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </>
  );
}