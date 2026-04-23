export default function DashboardHero() {
  return (
    <div className="mb-10">
      <div className="flex flex-col lg:flex-row justify-between items-start lg:items-center gap-6">
        <div>
          <p className="text-sky-400 font-medium mb-2 uppercase tracking-[0.2em] text-sm">
            AI Real Estate Intelligence
          </p>

          <h1 className="text-5xl font-bold leading-tight bg-gradient-to-r from-white to-slate-400 bg-clip-text text-transparent">
            Propwise AI Dashboard
          </h1>

          <p className="text-slate-400 mt-4 max-w-2xl text-lg">
            Analyze property investments instantly using AI-powered metrics,
            risk profiling, market comparisons, and profitability scoring.
          </p>
        </div>

        <div className="bg-slate-900/60 border border-slate-800 rounded-2xl px-5 py-4 backdrop-blur-lg">
          <p className="text-sm text-slate-400">Powered By</p>
          <p className="font-semibold text-white">LangGraph + OpenRouter + AI Agents</p>
        </div>
      </div>
    </div>
  );
}
