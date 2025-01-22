document.addEventListener('DOMContentLoaded', function() {
    const quotes = [
        "I can do all things through Christ who strengthens me. - Philippians 4:13",
        "For I know the plans I have for you, declares the Lord. - Jeremiah 29:11",
        "The Lord is my shepherd; I shall not want. - Psalm 23:1",
    ];

    const quoteElement = document.getElementById('daily-quote');
    const today = new Date().getDate();
    quoteElement.textContent = quotes[today % quotes.length];
});

console.log(quoteElement); // Check if the element is correctly selected
console.log(quotes[today % quotes.length]); // Check the quote being set
