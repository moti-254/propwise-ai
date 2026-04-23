interface Props {
  title: string;
  value: string | number;
  subtitle: string;
}

export default function MetricsCard({ title, value, subtitle }: Props) {
  return (
    <div className="bg-slate-900/70 border border-slate-800 rounded-3xl p-6 backdrop-blur-xl hover:border-sky-500/40 transition-all duration-300 hover:-translate-y-1">
      <p className="text-slate-400 text-sm mb-2">{title}</p>
      <h2 className="text-3xl font-bold text-white mb-2">{value}</h2>
      <p className="text-slate-500 text-sm">{subtitle}</p>
    </div>
  );
}
