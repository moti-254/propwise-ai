interface Props {
  explanation: string;
}

export default function ExplanationPanel({ explanation }: Props) {
  return (
    <div className="bg-slate-900/70 border border-slate-800 rounded-3xl p-6">
      <h2 className="text-xl font-semibold mb-5">AI Investment Explanation</h2>
      <div className="leading-8 text-slate-300 whitespace-pre-line text-[15px]">
        {explanation}
      </div>
    </div>
  );
}
