

import PropertyForm from "../components/PropertyForm";
import { usePropertyAnalysis } from "../hooks/usePropertyAnalysis";
import DashboardHero from "../components/dashboard/DashboardHero";
import MetricsCard from "../components/dashboard/MetricsCard";
import DecisionCard from "../components/dashboard/DecisionCard";
import RiskPanel from "../components/dashboard/RiskPanel";
import ExplanationPanel from "../components/dashboard/ExplanationPanel";
import MarketChart from "../components/dashboard/MarketChart";
import PropertySummary from "../components/dashboard/PropertySummary";
import LoadingState from "../components/dashboard/LoadingState";

import HowItWorks from "../components/HowItWorks";
import MetricsGuide from "../components/MetricsGuide";
import EmptyState from "../components/EmptyState";
import InvestmentTips from "../components/InvestmentTips";

export default function Dashboard() {
  const analysis = usePropertyAnalysis();

  return (
    <div className="min-h-screen bg-slate-950 text-white overflow-hidden">
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_top_right,#1e293b,transparent_40%)] opacity-70" />

      <div className="relative z-10 max-w-7xl mx-auto px-6 py-10 space-y-6">
        <div>
          <h1 className="text-4xl font-bold text-gray-900 mb-2">Propwise AI</h1>
          <p className="text-gray-600 text-lg">
            AI-powered property investment analysis and decision support.
          </p>
        </div>

        <HowItWorks />

        <div className="bg-slate-900/60 backdrop-blur-xl border border-slate-800 rounded-3xl p-6 shadow-2xl">
          <PropertyForm onSubmit={analysis.mutateAsync} />
        </div>

        {analysis.isPending && <LoadingState />}

        {analysis.isError && (
          <div className="bg-red-500/10 border border-red-500/30 rounded-2xl p-6 text-red-300">
            {analysis.error instanceof Error
              ? analysis.error.message
              : "Something went wrong."}
          </div>
        )}

        {!analysis.data && !analysis.isPending && <EmptyState />}

        {analysis.data && (
          <>
            <div className="space-y-8 animate-fade-in">
              <div className="grid md:grid-cols-2 xl:grid-cols-4 gap-5">
                <MetricsCard
                  title="ROI"
                  value={`${analysis.data.metrics?.roi?.toFixed(1)}%`}
                  subtitle="Return on Investment"
                />
                <MetricsCard
                  title="Rental Yield"
                  value={`${analysis.data.metrics?.rental_yield?.toFixed(1)}%`}
                  subtitle="Annual Yield"
                />
                <MetricsCard
                  title="Annual Profit"
                  value={`$${analysis.data.metrics?.annual_profit?.toLocaleString()}`}
                  subtitle="Profit Projection"
                />
                <MetricsCard
                  title="Risk Level"
                  value={analysis.data.risk?.risk_level}
                  subtitle={`Score ${analysis.data.risk?.risk_score}/10`}
                />
              </div>

              <div className="grid xl:grid-cols-3 gap-6">
                <div className="xl:col-span-2 space-y-6">
                  <PropertySummary data={analysis.data} />
                  <MarketChart data={analysis.data} />
                  <ExplanationPanel explanation={analysis.data.explanation} />
                </div>
                <div className="space-y-6">
                  <DecisionCard decision={analysis.data.decision} />
                  <RiskPanel risk={analysis.data.risk} />
                </div>
              </div>
            </div>
            <MetricsGuide />
            <InvestmentTips />
          </>
        )}
      </div>
    </div>
  );
}
