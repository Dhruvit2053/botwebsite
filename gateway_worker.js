/**
 * CineVibe / HDHub4u-Style Safe Domain Shield Worker
 * Deploy this on Cloudflare Workers on your main domain (e.g., hdhub4u.kz, cinevibe.kz, or cinevibe.com)
 *
 * HOW IT PROTECTS YOU:
 * 1. Your main domain NEVER hosts copyrighted content and NEVER gets DMCA strikes.
 * 2. When users visit your main domain, Cloudflare edge immediately redirects (302) to the active mirror (new16.xxx).
 * 3. If new16 mirror ever gets blocked, simply change ACTIVE_MIRROR to new17 in 5 seconds.
 */

const ACTIVE_MIRROR = "https://cinevibe-cinema.surge.sh";
const UTM_TAG = "utm=mn1";

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const userAgent = (request.headers.get("user-agent") || "").toLowerCase();

    // Preserve the original requested path and query parameters
    const targetUrl = new URL(ACTIVE_MIRROR);
    targetUrl.pathname = url.pathname;
    
    // Merge search parameters
    const params = new URLSearchParams(url.search);
    if (!params.has("utm")) {
      params.set("utm", "mn1");
    }
    targetUrl.search = params.toString();

    // OPTIONAL: If visited by copyright bot, you can serve a completely clean DMCA policy page
    if (userAgent.includes("dmca") || userAgent.includes("copyright") || userAgent.includes("crawler")) {
      return new Response(
        `<html><body style="background:#080808;color:#FFF;font-family:sans-serif;padding:40px;">
          <h2>CineVibe Rights & DMCA Verification Portal</h2>
          <p>This domain does not host, upload, or store any media files. It functions exclusively as a technology gateway.</p>
        </body></html>`,
        { headers: { "Content-Type": "text/html" } }
      );
    }

    // HTTP 302 Temporary Redirect to the active disposable mirror
    return Response.redirect(targetUrl.toString(), 302);
  }
};
