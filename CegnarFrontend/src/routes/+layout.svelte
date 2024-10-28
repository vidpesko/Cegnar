<script>
    // Custom css
    import "../app.css";
    // Splide js css
    import '@splidejs/svelte-splide/css';
    // Icons
    import IGIcon from '~icons/mdi/instagram';
    import FacebookIcon from '~icons/mdi/facebook-box';
    import EmailIcon from '~icons/mdi/email';
</script>

<slot />

<!-- Footer -->
<footer class="bg-background text-white border-t-[0.5px] relative">
    <div class="w-4/6 mx-auto">
        <!-- Columns -->
        <div class="pt-10 pb-4 md:flex-row flex flex-col justify-between items-start gap-8">
            <!-- 1. column - title, navigation -->
            <div class="footer-column">
                <div class="">
                    <h3 class="">Povezave</h3>
                </div>
                <ul>
                    <li>Domov</li>
                    <li>Galerija</li>
                    <li>Zgodba</li>
                    <li>Kontakt</li>
                </ul>
            </div>
            <!-- 2. column - contact, home address -->
            <div class="footer-column">
                <div class="">
                    <h3>Kontakt</h3>
                </div>
                <ul>
                    <li>
                        <EmailIcon />
                        <p>
                            064 182 101
                        </p>
                    </li>
                    <li>
                        <EmailIcon />
                        <p>
                            vid@pesko.si
                        </p>
                    </li>
                    <li style="align-items: start !important;">
                        <EmailIcon class="mt-[0.5px]" />
                        <p>
                            <b>Delavnica:</b><br>
                            Partizanska pot 17,<br>
                            4000 Kranj,<br>
                            Slovenija
                        </p>
                    </li>
                </ul>
            </div>
            <!-- 3. column - contact form -->
            <div class="footer-column">
                <div class="">
                    <h3>Pusti mi sporočilo</h3>
                </div>
                <form action="" class="flex flex-col gap-4 pt-2">
                    <!-- Name -->
                    <input type="text" class="input" placeholder="Ime" required>
                    <!-- Email -->
                    <input type="email" class="input" placeholder="Vaš email" required>
                    <!-- Message -->
                    <textarea name="" id="" rows="5" class="input resize-y" placeholder="Sporočilo" required></textarea>
                    <!-- Submit -->
                    <button type="submit" class="btn">POŠLJI</button>
                </form>
            </div>
        </div>
        
        <!-- Social & shoutout -->
        <div class="">
            <!-- Social -->
            <div class="py-5">
                <ul class="footer-social flex justify-center gap-4">
                    <li><a href="https://www.instagram.com/cegnarblacksmithing/"><IGIcon /></a></li>
                    <li><a href="https://www.instagram.com/cegnarblacksmithing/"><FacebookIcon /></a></li>
                    <li><a href="https://www.instagram.com/cegnarblacksmithing/"><EmailIcon /></a></li>
                </ul>
            </div>
            
        </div>
    </div>

    <!-- Designed by me -->
    <div class="w-full bg-red-400 text-center">
        <a>Izdelal Vid</a>
    </div>
</footer>
