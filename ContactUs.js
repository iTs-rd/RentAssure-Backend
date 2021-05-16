import React, { Component } from "react";
import "../css/ContactUs.css";

class ContactUs extends Component {
    constructor() {
        super();
        this.state = {
            name: "",
            email: "",
            mobile: "",
            detail: "",
        };
        this.changeHandler = this.changeHandler.bind(this);
        this.submitForm = this.submitForm.bind(this);
    }

    // Input Change Handler
    changeHandler(event) {
        this.setState({
            [event.target.name]: event.target.value,
        });
        console.log(this.state);
    }

    // Submit Form
    submitForm() {
        var frm = document.getElementById("contact-form");
        // console.log(JSON.stringify(this.state));
        var f = new FormData(frm);
        console.log(f);
        alert(f);
        fetch("http://127.0.0.1:8000/api/contact/", {
            method: "POST",
            body: JSON.stringify(this.state),
            headers: {
                "Content-type": "application/json",
            },
        })
            .then((response) => response.json())
            .then((data) => console.log(data));

        this.setState({
            name: " ",
            email: " ",
            mobile: " ",
            detail: " ",
        });
    }
    render() {
        return (
            <React.Fragment>
                <section>
                    <div class="container">
                        <div class="wrapper">
                            <div class="contact-info">
                                <h2>Contact Info</h2>

                                <ul class="info">
                                    <li>
                                        <i class="fa fa-road fa-2x"></i> 2252 Brooklyn Street
                                        <br />
                                        Washington, USA
                                        <br />
                                        92313
                                    </li>
                                    <br />
                                    <li>
                                        <i class="fa fa-envelope fa-2x"></i> lorem@ipsum.com
                                    </li>
                                    <br />
                                    <li>
                                        <i class="fa fa-phone fa-2x"></i> +918858896086
                                    </li>
                                </ul>
                                <ul class="sci">
                                    <br />
                                    <li>
                                        <a href="#" alt="Facebook">
                                            <ion-icon name="logo-facebook" size="large"></ion-icon>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#" alt="Twitter">
                                            <ion-icon name="logo-twitter" size="large"></ion-icon>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#" alt="Instagram">
                                            <ion-icon name="logo-instagram" size="large"></ion-icon>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#" alt="Linkedin">
                                            <ion-icon name="logo-linkedin" size="large"></ion-icon>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#" alt="Quora">
                                            <ion-icon name="people-outline" size="large"></ion-icon>
                                        </a>
                                    </li>
                                </ul>
                            </div>

                            <div class="contact">
                                <h2>Send Message</h2>

                                <form id="contact-form">
                                    <p>
                                        <label>Name</label>
                                        <input type="text" name="name" id="name" onChange={this.changeHandler} value={this.state.name} />
                                    </p>

                                    <p>
                                        <label>E-mail Address</label>
                                        <input type="email" name="email" id="email" onChange={this.changeHandler} value={this.state.email} />
                                    </p>

                                    <p>
                                        <label>Mobile Number</label>
                                        <input type="text" name="mobile" value={this.state.mobile} onChange={this.changeHandler} id="mobileNumber" />
                                    </p>

                                    <p class="full">
                                        <label>Write your message here...</label>
                                        <input
                                            type="text"
                                            name="detail"
                                            value={this.state.detail}
                                            onChange={this.changeHandler}
                                            rows="5"
                                            id="message"
                                            class="message"
                                        />
                                    </p>

                                    <p class="full">
                                        <input type="submit" onClick={this.submitForm} class="btn btn-primary" />
                                    </p>
                                </form>
                            </div>
                        </div>
                    </div>
                </section>
            </React.Fragment>
        );
    }
}

export default ContactUs;
