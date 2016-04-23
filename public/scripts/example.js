var CommentList = React.createClass({
    render: function() {
        return (
            <div>Comment list!</div>
        );
    }
});

var CommentForm = React.createClass({
    render: function() {
        return (
            <div>Comment form!</div>
        );
    }
});

var CommentBox = React.createClass({
    render: function() {
        return (
            <div>
                <h1>Comments</h1>
                <CommentList />
                <CommentForm />
            </div>
        );
    }
});

ReactDOM.render(
    <CommentBox />,
    document.getElementById('content')
);
