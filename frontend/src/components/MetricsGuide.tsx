export default function MetricsGuide() {
  return (
    <div className="bg-white rounded-2xl shadow-sm border border-gray-200 p-6 mt-6">
      <h2 className="text-xl font-bold mb-4 text-gray-900">
        How Metrics Are Calculated
      </h2>

      <div className="space-y-4 text-sm text-gray-700">
        <Metric
          title="ROI"
          formula="(Annual Profit ÷ Property Price) × 100"
        />

        <Metric
          title="Rental Yield"
          formula="(Monthly Rent × 12 ÷ Property Price) × 100"
        />

        <Metric
          title="Cap Rate"
          formula="Net Operating Income ÷ Property Price"
        />

        <Metric
          title="Risk Score"
          formula="Based on market demand, pricing, vacancy, and growth indicators"
        />
      </div>
    </div>
  )
}

function Metric({ title, formula }: any) {
  return (
    <div className="border-b border-gray-100 pb-3">
      <div className="font-semibold text-gray-900 mb-1">
        {title}
      </div>

      <div className="text-gray-600">
        {formula}
      </div>
    </div>
  )
}
