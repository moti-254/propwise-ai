interface Props {
  decision: any;
}

export default function DecisionCard({ decision }: Props) {
  const verdictColor =
    decision?.verdict === "Good Investment"
      ? "bg-green-500/20 text-green-400 border-green-500/30"
      : "bg-red-500/20 text-red-400 border-red-500/30";

  return (
    <div className="bg-slate-900/70 border border-slate-800 rounded-3xl p-6">
      <h2 className="text-xl font-semibold mb-5">Investment Verdict</h2>
      <div className={`rounded-2xl border px-4 py-5 ${verdictColor}`}>
        <p className="text-sm opacity-80 mb-2">Decision</p>
        <h3 className="text-2xl font-bold">{decision?.verdict}</h3>
      </div>
      <div className="mt-6 space-y-3">
        <div>
          <p className="text-slate-400 text-sm">Confidence</p>
          <div className="w-full bg-slate-800 rounded-full h-3 mt-2 overflow-hidden">
            <div
              className="bg-sky-500 h-full rounded-full"
              style={{ width: `${(decision?.confidence || 0) * 100}%` }}
            />
          </div>
        </div>
        <div>
          <p className="text-slate-400 text-sm">AI Score</p>
          <h3 className="text-2xl font-bold mt-1">
            {decision?.score}/10
          </h3>
        </div>
      </div>
    </div>
  );
}
