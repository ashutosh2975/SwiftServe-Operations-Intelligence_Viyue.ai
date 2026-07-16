import { useState } from "react";
import ReactMarkdown from "react-markdown";
import { getMorningBrief } from "../services/api";

export default function MorningBrief() {
  const [brief, setBrief] = useState("");
  const [loading, setLoading] = useState(false);

  const generateBrief = async () => {
    try {
      setLoading(true);

      const response = await getMorningBrief();

      setBrief(response.data.brief);
    } catch (error) {
      console.error("Error generating brief:", error);

      setBrief(
        "Unable to generate AI brief. Please check backend connection."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white rounded-xl shadow-md p-6 mb-6">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-3xl font-bold text-gray-800">
          AI Morning Brief
        </h2>

        <button
          onClick={generateBrief}
          disabled={loading}
          className="bg-blue-600 hover:bg-blue-700 text-white px-5 py-2 rounded-lg font-medium transition"
        >
          {loading ? "Generating..." : "Generate Brief"}
        </button>
      </div>

      {loading && (
        <div className="bg-blue-50 border border-blue-200 p-4 rounded-lg">
          <p className="animate-pulse text-blue-700">
            Generating AI Brief...
          </p>
        </div>
      )}

      {!loading && brief && (
        <div className="bg-gray-50 border border-gray-200 p-5 rounded-lg">
          <div className="prose max-w-none">
            <ReactMarkdown>
              {brief}
            </ReactMarkdown>
          </div>
        </div>
      )}

      {!loading && !brief && (
        <div className="bg-gray-50 border border-dashed border-gray-300 p-5 rounded-lg text-gray-500">
          Click <strong>Generate Brief</strong> to create an AI-powered operational summary.
        </div>
      )}
    </div>
  );
}