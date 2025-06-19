import { auth, provider } from "../firebase";
import { signInWithPopup } from "firebase/auth";

export default function SignInButton() {
  const handleLogin = async () => {
    try {
      const result = await signInWithPopup(auth, provider);
      const user = result.user;
      console.log("✅ Signed in:", user.displayName);
    } catch (error) {
      console.error("❌ Sign-in error:", error);
    }
  };

  return (
    <button
      onClick={handleLogin}
      className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md"
    >
      Sign in with Google
    </button>
  );
}
