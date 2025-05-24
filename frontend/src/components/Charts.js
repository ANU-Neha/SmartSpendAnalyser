import { Bar, Pie } from 'react-chartjs-2';
import { Chart as ChartJS, registerables } from 'chart.js';
ChartJS.register(...registerables);

export function BarChart() {
  const data = {
    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    datasets: [
      {
        label: 'Spending',
        data: [1200, 1900, 1500, 2000, 1800, 2200],
        backgroundColor: 'rgba(211, 47, 47, 0.6)',
        borderColor: 'rgba(211, 47, 47, 1)',
        borderWidth: 1,
      },
    ],
  };

  return <Bar data={data} />;
}

export function PieChart() {
  const data = {
    labels: ['Food', 'Transport', 'Entertainment', 'Utilities', 'Other'],
    datasets: [
      {
        data: [35, 25, 15, 15, 10],
        backgroundColor: [
          'rgba(211, 47, 47, 0.6)',
          'rgba(176, 190, 197, 0.6)',
          'rgba(229, 115, 115, 0.6)',
          'rgba(207, 216, 220, 0.6)',
          'rgba(239, 154, 154, 0.6)',
        ],
        borderColor: [
          'rgba(211, 47, 47, 1)',
          'rgba(176, 190, 197, 1)',
          'rgba(229, 115, 115, 1)',
          'rgba(207, 216, 220, 1)',
          'rgba(239, 154, 154, 1)',
        ],
        borderWidth: 1,
      },
    ],
  };

  return <Pie data={data} />;
}