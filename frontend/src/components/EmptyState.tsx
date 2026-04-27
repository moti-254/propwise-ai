export default function EmptyState() {
  return (
    <div className="bg-gradient-to-br from-indigo-50 to-white border border-indigo-100 rounded-2xl p-10 text-center">
      <h2 className="text-2xl font-bold text-gray-900 mb-3">
        Start Your Property Analysis
      </h2>

      <p className="text-gray-600 max-w-2xl mx-auto mb-6">
        Enter property details to receive ROI projections, rental yield,
        market comparables, risk analysis, and an AI-generated investment recommendation.
      </p>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-6 text-sm">
        <Badge label="ROI Analysis" />
        <Badge label="Market Comparables" />
        <Badge label="Risk Assessment" />
        <Badge label="Investment Score" />
      </div>
    </div>
  )
}

function Badge({ label }: any) {
  return (
    <div className="bg-slate-800 border border-gray-700 rounded-xl py-3 px-4 shadow-sm text-white">
      {label}
    </div>
  )
}
