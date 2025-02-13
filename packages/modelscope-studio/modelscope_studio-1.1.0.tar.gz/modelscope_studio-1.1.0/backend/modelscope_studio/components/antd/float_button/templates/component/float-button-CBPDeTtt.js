import { i as se, a as W, r as le, g as ce, w as T } from "./Index-DoCk_V5K.js";
const w = window.ms_globals.React, ne = window.ms_globals.React.forwardRef, re = window.ms_globals.React.useRef, oe = window.ms_globals.React.useState, ie = window.ms_globals.React.useEffect, A = window.ms_globals.ReactDOM.createPortal, ae = window.ms_globals.internalContext.useContextPropsContext, ue = window.ms_globals.antd.FloatButton;
var de = /\s/;
function fe(e) {
  for (var t = e.length; t-- && de.test(e.charAt(t)); )
    ;
  return t;
}
var me = /^\s+/;
function pe(e) {
  return e && e.slice(0, fe(e) + 1).replace(me, "");
}
var M = NaN, _e = /^[-+]0x[0-9a-f]+$/i, he = /^0b[01]+$/i, ge = /^0o[0-7]+$/i, be = parseInt;
function U(e) {
  if (typeof e == "number")
    return e;
  if (se(e))
    return M;
  if (W(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = W(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = pe(e);
  var o = he.test(e);
  return o || ge.test(e) ? be(e.slice(2), o ? 2 : 8) : _e.test(e) ? M : +e;
}
var j = function() {
  return le.Date.now();
}, ye = "Expected a function", Ee = Math.max, we = Math.min;
function xe(e, t, o) {
  var s, i, n, r, l, u, p = 0, g = !1, c = !1, b = !0;
  if (typeof e != "function")
    throw new TypeError(ye);
  t = U(t) || 0, W(o) && (g = !!o.leading, c = "maxWait" in o, n = c ? Ee(U(o.maxWait) || 0, t) : n, b = "trailing" in o ? !!o.trailing : b);
  function m(d) {
    var y = s, R = i;
    return s = i = void 0, p = d, r = e.apply(R, y), r;
  }
  function x(d) {
    return p = d, l = setTimeout(h, t), g ? m(d) : r;
  }
  function f(d) {
    var y = d - u, R = d - p, D = t - y;
    return c ? we(D, n - R) : D;
  }
  function _(d) {
    var y = d - u, R = d - p;
    return u === void 0 || y >= t || y < 0 || c && R >= n;
  }
  function h() {
    var d = j();
    if (_(d))
      return v(d);
    l = setTimeout(h, f(d));
  }
  function v(d) {
    return l = void 0, b && s ? m(d) : (s = i = void 0, r);
  }
  function C() {
    l !== void 0 && clearTimeout(l), p = 0, s = u = i = l = void 0;
  }
  function a() {
    return l === void 0 ? r : v(j());
  }
  function I() {
    var d = j(), y = _(d);
    if (s = arguments, i = this, u = d, y) {
      if (l === void 0)
        return x(u);
      if (c)
        return clearTimeout(l), l = setTimeout(h, t), m(u);
    }
    return l === void 0 && (l = setTimeout(h, t)), r;
  }
  return I.cancel = C, I.flush = a, I;
}
var Y = {
  exports: {}
}, P = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var ve = w, Ce = Symbol.for("react.element"), Ie = Symbol.for("react.fragment"), Se = Object.prototype.hasOwnProperty, Re = ve.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Oe = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function Q(e, t, o) {
  var s, i = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (s in t) Se.call(t, s) && !Oe.hasOwnProperty(s) && (i[s] = t[s]);
  if (e && e.defaultProps) for (s in t = e.defaultProps, t) i[s] === void 0 && (i[s] = t[s]);
  return {
    $$typeof: Ce,
    type: e,
    key: n,
    ref: r,
    props: i,
    _owner: Re.current
  };
}
P.Fragment = Ie;
P.jsx = Q;
P.jsxs = Q;
Y.exports = P;
var E = Y.exports;
const {
  SvelteComponent: Te,
  assign: z,
  binding_callbacks: G,
  check_outros: ke,
  children: Z,
  claim_element: $,
  claim_space: Le,
  component_subscribe: H,
  compute_slots: Pe,
  create_slot: je,
  detach: S,
  element: ee,
  empty: K,
  exclude_internal_props: q,
  get_all_dirty_from_scope: Ne,
  get_slot_changes: Ae,
  group_outros: We,
  init: Fe,
  insert_hydration: k,
  safe_not_equal: Be,
  set_custom_element_data: te,
  space: De,
  transition_in: L,
  transition_out: F,
  update_slot_base: Me
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ue,
  getContext: ze,
  onDestroy: Ge,
  setContext: He
} = window.__gradio__svelte__internal;
function V(e) {
  let t, o;
  const s = (
    /*#slots*/
    e[7].default
  ), i = je(
    s,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = ee("svelte-slot"), i && i.c(), this.h();
    },
    l(n) {
      t = $(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = Z(t);
      i && i.l(r), r.forEach(S), this.h();
    },
    h() {
      te(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      k(n, t, r), i && i.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      i && i.p && (!o || r & /*$$scope*/
      64) && Me(
        i,
        s,
        n,
        /*$$scope*/
        n[6],
        o ? Ae(
          s,
          /*$$scope*/
          n[6],
          r,
          null
        ) : Ne(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (L(i, n), o = !0);
    },
    o(n) {
      F(i, n), o = !1;
    },
    d(n) {
      n && S(t), i && i.d(n), e[9](null);
    }
  };
}
function Ke(e) {
  let t, o, s, i, n = (
    /*$$slots*/
    e[4].default && V(e)
  );
  return {
    c() {
      t = ee("react-portal-target"), o = De(), n && n.c(), s = K(), this.h();
    },
    l(r) {
      t = $(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), Z(t).forEach(S), o = Le(r), n && n.l(r), s = K(), this.h();
    },
    h() {
      te(t, "class", "svelte-1rt0kpf");
    },
    m(r, l) {
      k(r, t, l), e[8](t), k(r, o, l), n && n.m(r, l), k(r, s, l), i = !0;
    },
    p(r, [l]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, l), l & /*$$slots*/
      16 && L(n, 1)) : (n = V(r), n.c(), L(n, 1), n.m(s.parentNode, s)) : n && (We(), F(n, 1, 1, () => {
        n = null;
      }), ke());
    },
    i(r) {
      i || (L(n), i = !0);
    },
    o(r) {
      F(n), i = !1;
    },
    d(r) {
      r && (S(t), S(o), S(s)), e[8](null), n && n.d(r);
    }
  };
}
function J(e) {
  const {
    svelteInit: t,
    ...o
  } = e;
  return o;
}
function qe(e, t, o) {
  let s, i, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const l = Pe(n);
  let {
    svelteInit: u
  } = t;
  const p = T(J(t)), g = T();
  H(e, g, (a) => o(0, s = a));
  const c = T();
  H(e, c, (a) => o(1, i = a));
  const b = [], m = ze("$$ms-gr-react-wrapper"), {
    slotKey: x,
    slotIndex: f,
    subSlotIndex: _
  } = ce() || {}, h = u({
    parent: m,
    props: p,
    target: g,
    slot: c,
    slotKey: x,
    slotIndex: f,
    subSlotIndex: _,
    onDestroy(a) {
      b.push(a);
    }
  });
  He("$$ms-gr-react-wrapper", h), Ue(() => {
    p.set(J(t));
  }), Ge(() => {
    b.forEach((a) => a());
  });
  function v(a) {
    G[a ? "unshift" : "push"](() => {
      s = a, g.set(s);
    });
  }
  function C(a) {
    G[a ? "unshift" : "push"](() => {
      i = a, c.set(i);
    });
  }
  return e.$$set = (a) => {
    o(17, t = z(z({}, t), q(a))), "svelteInit" in a && o(5, u = a.svelteInit), "$$scope" in a && o(6, r = a.$$scope);
  }, t = q(t), [s, i, g, c, l, u, r, n, v, C];
}
class Ve extends Te {
  constructor(t) {
    super(), Fe(this, t, qe, Ke, Be, {
      svelteInit: 5
    });
  }
}
const X = window.ms_globals.rerender, N = window.ms_globals.tree;
function Je(e, t = {}) {
  function o(s) {
    const i = T(), n = new Ve({
      ...s,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const l = {
            key: window.ms_globals.autokey,
            svelteInstance: i,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, u = r.parent ?? N;
          return u.nodes = [...u.nodes, l], X({
            createPortal: A,
            node: N
          }), r.onDestroy(() => {
            u.nodes = u.nodes.filter((p) => p.svelteInstance !== i), X({
              createPortal: A,
              node: N
            });
          }), l;
        },
        ...s.props
      }
    });
    return i.set(n), n;
  }
  return new Promise((s) => {
    window.ms_globals.initializePromise.then(() => {
      s(o);
    });
  });
}
const Xe = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function Ye(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const s = e[o];
    return t[o] = Qe(o, s), t;
  }, {}) : {};
}
function Qe(e, t) {
  return typeof t == "number" && !Xe.includes(e) ? t + "px" : t;
}
function B(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const i = w.Children.toArray(e._reactElement.props.children).map((n) => {
      if (w.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: l
        } = B(n.props.el);
        return w.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...w.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return i.originalChildren = e._reactElement.props.children, t.push(A(w.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: i
    }), o)), {
      clonedElement: o,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((i) => {
    e.getEventListeners(i).forEach(({
      listener: r,
      type: l,
      useCapture: u
    }) => {
      o.addEventListener(l, r, u);
    });
  });
  const s = Array.from(e.childNodes);
  for (let i = 0; i < s.length; i++) {
    const n = s[i];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: l
      } = B(n);
      t.push(...l), o.appendChild(r);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: t
  };
}
function Ze(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const O = ne(({
  slot: e,
  clone: t,
  className: o,
  style: s,
  observeAttributes: i
}, n) => {
  const r = re(), [l, u] = oe([]), {
    forceClone: p
  } = ae(), g = p ? !0 : t;
  return ie(() => {
    var x;
    if (!r.current || !e)
      return;
    let c = e;
    function b() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), Ze(n, f), o && f.classList.add(...o.split(" ")), s) {
        const _ = Ye(s);
        Object.keys(_).forEach((h) => {
          f.style[h] = _[h];
        });
      }
    }
    let m = null;
    if (g && window.MutationObserver) {
      let f = function() {
        var C, a, I;
        (C = r.current) != null && C.contains(c) && ((a = r.current) == null || a.removeChild(c));
        const {
          portals: h,
          clonedElement: v
        } = B(e);
        c = v, u(h), c.style.display = "contents", b(), (I = r.current) == null || I.appendChild(c);
      };
      f();
      const _ = xe(() => {
        f(), m == null || m.disconnect(), m == null || m.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: i
        });
      }, 50);
      m = new window.MutationObserver(_), m.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", b(), (x = r.current) == null || x.appendChild(c);
    return () => {
      var f, _;
      c.style.display = "", (f = r.current) != null && f.contains(c) && ((_ = r.current) == null || _.removeChild(c)), m == null || m.disconnect();
    };
  }, [e, g, o, s, n, i]), w.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
}), et = Je(({
  slots: e,
  children: t,
  ...o
}) => {
  var s;
  return /* @__PURE__ */ E.jsxs(E.Fragment, {
    children: [/* @__PURE__ */ E.jsx("div", {
      style: {
        display: "none"
      },
      children: t
    }), /* @__PURE__ */ E.jsx(ue, {
      ...o,
      icon: e.icon ? /* @__PURE__ */ E.jsx(O, {
        clone: !0,
        slot: e.icon
      }) : o.icon,
      description: e.description ? /* @__PURE__ */ E.jsx(O, {
        clone: !0,
        slot: e.description
      }) : o.description,
      tooltip: e.tooltip ? /* @__PURE__ */ E.jsx(O, {
        clone: !0,
        slot: e.tooltip
      }) : o.tooltip,
      badge: {
        ...o.badge,
        count: e["badge.count"] ? /* @__PURE__ */ E.jsx(O, {
          slot: e["badge.count"]
        }) : (s = o.badge) == null ? void 0 : s.count
      }
    })]
  });
});
export {
  et as FloatButton,
  et as default
};
