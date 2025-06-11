document.addEventListener("DOMContentLoaded", () => {
  const chatForm = document.getElementById("chat-form");
  const userInput = document.getElementById("user-input");
  const chatMessages = document.getElementById("chat-messages");
  let questionCount = 0;
  let ctaAppended = false;

  chatForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const message = userInput.value.trim();
    if (!message) return;

    appendMessage(message, "user-message");
    userInput.value = "";
    userInput.disabled = true;

    const typingDiv = appendTypingIndicator();

    try {
      const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
      });

      const data = await response.json();
      const replyText = data.reply || "";

      const delay = calculateTypingDelay(replyText);
      await delayMs(delay);

      typingDiv.remove();

      const hasCTA = replyText.includes("{{cta}}");
      const cleanReply = replyText.replace("{{cta}}", "").trim();
      appendMessage(cleanReply, "bot-message");

      questionCount++;

      const triggerKeywords = [
        "book an appointment",
        "schedule a call",
        "book now",
        "call now",
        "book a call",
        "schedule a meeting",
        "book a meeting",
        "i want to book",
        "schedule appointment",
        "book a session",
        "make an appointment",
        "schedule a session"
      ];

      const shouldShowCTA =
        hasCTA ||
        questionCount === 9 ||
        triggerKeywords.some(k => replyText.toLowerCase().includes(k));

      if (shouldShowCTA) {
        appendCTAButtons(questionCount === 9); // true = motivational version
      }

    } catch (err) {
      typingDiv.remove();
      appendMessage("⚠️ Error contacting the server.", "bot-message");
      console.error("Fetch error:", err);
    } finally {
      userInput.disabled = false;
      userInput.focus();
    }
  });

  function appendMessage(text, className) {
    const msg = document.createElement("div");
    msg.className = `message ${className}`;
    msg.textContent = text;
    chatMessages.appendChild(msg);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  function appendTypingIndicator() {
    const typing = document.createElement("div");
    typing.className = "message typing-indicator";
    chatMessages.appendChild(typing);
    chatMessages.scrollTop = chatMessages.scrollHeight;
    return typing;
  }

  function delayMs(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }

  function calculateTypingDelay(text) {
    const baseDelay = 300;
    const chars = text.length;
    const variableDelay = Math.min(chars * 20, 2000); // Max 2s
    return baseDelay + variableDelay;
  }

  function appendCTAButtons(triggeredByCount = false) {
    if (ctaAppended) return;
    ctaAppended = true;

    const cta = document.createElement("div");
    cta.className = "message bot-message";

    let introMessage = "";

    if (triggeredByCount) {
      introMessage = `
        <p>If you’ve made it this far, you probably have questions best answered by a specialist.</p>
        <p><strong>Let’s make it easy — book a call now and talk directly with one of our specialists.</strong></p>
      `;
    }

    cta.innerHTML = `
      ${introMessage}
      <button class="cta-button" onclick="window.location.href='tel:+1234567890'">📞 Call Now</button>
      <button class="cta-button" onclick="window.location.href='https://your-booking-link.com'">📅 Book an Appointment</button>
    `;
    chatMessages.appendChild(cta);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }
});
