export default function LoadingState() {
  return (
    <div className="bg-slate-900/70 border border-slate-800 rounded-3xl p-10 flex flex-col items-center justify-center text-center">
      <div className="flex gap-2 mb-5">
        <div className="w-4 h-4 rounded-full bg-sky-400 animate-bounce" />
        <div className="w-4 h-4 rounded-full bg-indigo-400 animate-bounce delay-100" />
        <div className="w-4 h-4 rounded-full bg-purple-400 animate-bounce delay-200" />
      </div>
      <h2 className="text-2xl font-bold mb-2">Analyzing Property</h2>
      <p className="text-slate-400">
        AI agents are evaluating profitability, risk and market insights.
      </p>
    </div>
  );
}
