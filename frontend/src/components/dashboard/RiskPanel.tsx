interface Props {
  risk: any;
}

export default function RiskPanel({ risk }: Props) {
  return (
    <div className="bg-slate-900/70 border border-slate-800 rounded-3xl p-6">
      <h2 className="text-xl font-semibold mb-5">Risk Analysis</h2>
      <div className="space-y-3">
        {risk?.risks?.map((riskItem: string, index: number) => (
          <div
            key={index}
            className="bg-slate-800/60 border border-slate-700 rounded-xl p-4"
          >
            <p className="text-slate-300">{riskItem}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
