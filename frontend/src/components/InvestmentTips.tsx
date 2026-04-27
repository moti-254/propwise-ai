export default function InvestmentTips() {
  return (
    <div className="bg-white rounded-2xl shadow-sm border border-gray-200 p-6 mt-6">
      <h2 className="text-xl font-bold mb-4 text-gray-900">
        What Makes a Good Investment Property?
      </h2>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <Tip text="ROI above 8%" />
        <Tip text="Rental Yield above 6%" />
        <Tip text="Low vacancy markets" />
        <Tip text="Growing neighborhoods" />
        <Tip text="Strong rental demand" />
        <Tip text="Competitive property pricing" />
      </div>
    </div>
  )
}

function Tip({ text }: any) {
  return (
    <div className="bg-gray-50 rounded-xl border border-gray-100 p-4 text-sm text-gray-700">
      {text}
    </div>
  )
}
