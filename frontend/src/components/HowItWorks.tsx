export default function HowItWorks() {
  return (
    <div className="bg-white rounded-2xl shadow-sm border border-gray-200 p-6 mb-6">
      <h2 className="text-2xl font-bold mb-3 text-gray-900">
        How Propwise AI Works
      </h2>

      <p className="text-gray-600 mb-6">
        Analyze a property’s investment potential using financial metrics,
        market comparables, rental demand, and AI-powered risk scoring.
      </p>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Step
          number="1"
          title="Input Property"
          desc="Enter price, rent, location, and property details."
        />

        <Step
          number="2"
          title="Market Analysis"
          desc="We compare similar nearby properties and market trends."
        />

        <Step
          number="3"
          title="Financial Metrics"
          desc="ROI, rental yield, cap rate, and profitability are calculated."
        />

        <Step
          number="4"
          title="Investment Decision"
          desc="AI evaluates risk and recommends investment quality."
        />
      </div>
    </div>
  )
}

function Step({ number, title, desc }: any) {
  return (
    <div className="bg-gray-50 rounded-xl p-4 border border-gray-100">
      <div className="text-sm font-bold text-indigo-600 mb-2">
        Step {number}
      </div>

      <h3 className="font-semibold text-gray-900 mb-1">
        {title}
      </h3>

      <p className="text-sm text-gray-600">
        {desc}
      </p>
    </div>
  )
}
