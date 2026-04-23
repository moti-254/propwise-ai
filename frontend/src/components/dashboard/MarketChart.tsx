import {
  ResponsiveContainer,
  BarChart,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
  Bar,
} from "recharts";

interface Props {
  data: any;
}

export default function MarketChart({ data }: Props) {
  const chartData = [
    {
      name: "Property",
      price: data.property.price,
      rent: data.property.expected_rent,
    },
    {
      name: "Market Avg",
      price: data.market.average_price,
      rent: data.market.average_rent,
    },
  ];

  return (
    <div className="bg-slate-900/70 border border-slate-800 rounded-3xl p-6 h-[420px]">
      <h2 className="text-xl font-semibold mb-6">Market Comparison</h2>
      <ResponsiveContainer width="100%" height="90%">
        <BarChart data={chartData}>
          <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
          <XAxis dataKey="name" stroke="#94a3b8" />
          <YAxis stroke="#94a3b8" />
          <Tooltip />
          <Bar dataKey="price" fill="#38bdf8" radius={[8, 8, 0, 0]} />
          <Bar dataKey="rent" fill="#6366f1" radius={[8, 8, 0, 0]} />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
