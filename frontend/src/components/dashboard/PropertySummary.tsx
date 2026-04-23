interface Props {
  data: any;
}

export default function PropertySummary({ data }: Props) {
  return (
    <div className="bg-slate-900/70 border border-slate-800 rounded-3xl p-6">
      <h2 className="text-xl font-semibold mb-6">Property Overview</h2>
      <div className="grid md:grid-cols-2 gap-6 text-sm">
        <div>
          <p className="text-slate-400">Location</p>
          <p className="text-lg font-semibold">{data.property.location}</p>
        </div>
        <div>
          <p className="text-slate-400">Price</p>
          <p className="text-lg font-semibold">
            ${data.property.price.toLocaleString()}
          </p>
        </div>
        <div>
          <p className="text-slate-400">Expected Rent</p>
          <p className="text-lg font-semibold">
            ${data.property.expected_rent}/month
          </p>
        </div>
        <div>
          <p className="text-slate-400">Market Average</p>
          <p className="text-lg font-semibold">
            ${data.market.average_price}
          </p>
        </div>
      </div>
    </div>
  );
}
